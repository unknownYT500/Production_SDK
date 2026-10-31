#!/usr/bin/env python3
"""
Sovereign AI Governance SDK: Autonomous Conversation Archiver
Parses Antigravity JSONL transcripts and formats them into clean,
timestamped Markdown logs saved directly inside the project folder (.ai_transcripts/).

Can be executed:
1. As an Antigravity Lifecycle Hook (stdin JSON payload on Stop / PostInvocation).
2. As a standalone CLI tool or script.
"""

import sys
import os
import json
import re
import argparse
from pathlib import Path
from datetime import datetime, timezone

# Ensure UTF-8 console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

DEFAULT_APP_DATA = Path(os.environ.get('USERPROFILE', '')) / ".gemini" / "antigravity-ide"

def clean_user_prompt(raw_content: str) -> str:
    """Extract clean user request from <USER_REQUEST> tags if present."""
    match = re.search(r'<USER_REQUEST>\s*(.*?)\s*</USER_REQUEST>', raw_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_content.strip()

def format_timestamp(iso_str: str) -> str:
    """Format ISO timestamp to readable string."""
    try:
        dt = datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except Exception:
        return iso_str

def parse_transcript_jsonl(transcript_path: Path) -> list:
    """Parse JSONL transcript file into list of message events."""
    events = []
    if not transcript_path.exists():
        return events

    with open(transcript_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                events.append(data)
            except json.JSONDecodeError:
                continue
    return events

def generate_markdown_transcript(conversation_id: str, events: list, project_name: str = "Project") -> str:
    """Convert parsed events into a structured, human-readable Markdown log."""
    lines = [
        f"# AI Conversation Transcript & Trajectory Log",
        f"> **Project:** {project_name}  ",
        f"> **Conversation ID:** `{conversation_id}`  ",
        f"> **Archived At:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  ",
        f"> **Total Steps Logged:** {len(events)}  ",
        "",
        "---",
        ""
    ]

    turn_count = 0
    for event in events:
        source = event.get('source', '')
        step_type = event.get('type', '')
        created_at = format_timestamp(event.get('created_at', ''))
        content = event.get('content', '')
        tool_calls = event.get('tool_calls', [])

        if step_type == 'USER_INPUT':
            turn_count += 1
            cleaned_text = clean_user_prompt(content)
            lines.extend([
                f"## 👤 Turn {turn_count}: User Prompt",
                f"*Timestamp:* `{created_at}`",
                "",
                "```text",
                cleaned_text,
                "```",
                "",
                "---",
                ""
            ])

        elif step_type == 'PLANNER_RESPONSE' or source == 'MODEL':
            if content or tool_calls:
                lines.extend([
                    f"### 🤖 Agent Response",
                    f"*Timestamp:* `{created_at}`",
                    ""
                ])

                if content:
                    lines.extend([
                        content.strip(),
                        ""
                    ])

                if tool_calls:
                    lines.extend([
                        "<details>",
                        f"<summary>🛠️ Executed {len(tool_calls)} Tool Calls (click to expand)</summary>",
                        "",
                    ])
                    for tc in tool_calls:
                        name = tc.get('name', 'tool')
                        args = tc.get('args', {})
                        lines.append(f"- **Tool:** `{name}`")
                        lines.append(f"  ```json\n  {json.dumps(args, indent=2)}\n  ```")
                    lines.extend([
                        "",
                        "</details>",
                        ""
                    ])

                lines.extend(["---", ""])

    return "\n".join(lines)

def run_archiver(transcript_path: Path, output_dir: Path, conversation_id: str = "unknown", project_name: str = "Project") -> Path:
    """Execute parsing and write transcript file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    events = parse_transcript_jsonl(transcript_path)
    
    if not events:
        print(f"[!] No events found in {transcript_path}")
        return None

    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f"conversation_{conversation_id[:8]}_{date_str}.md"
    output_file = output_dir / output_filename
    
    md_content = generate_markdown_transcript(conversation_id, events, project_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"[+] Successfully archived conversation to: {output_file.resolve()}")
    return output_file

def main():
    parser = argparse.ArgumentParser(description="Archive Antigravity Conversation Transcripts into Project Folder.")
    parser.add_argument("--hook", action="store_true", help="Run in Antigravity Lifecycle Hook mode (reads JSON from stdin)")
    parser.add_argument("--transcript-path", help="Direct path to transcript.jsonl")
    parser.add_argument("--conversation-id", help="Conversation ID to locate transcript in brain directory")
    parser.add_argument("--output-dir", default=".ai_transcripts", help="Output directory inside project")
    parser.add_argument("--project-name", default="Sovereign Project", help="Name of project")
    args = parser.parse_args()

    # 1. Check if explicitly invoked via Antigravity Lifecycle Hook
    if args.hook:
        try:
            stdin_data = sys.stdin.read().strip()
            if stdin_data:
                payload = json.loads(stdin_data)
                conversation_id = payload.get('conversationId', 'unknown')
                transcript_str = payload.get('transcriptPath')
                workspace_paths = payload.get('workspacePaths', ['.'])
                project_root = Path(workspace_paths[0]) if workspace_paths else Path('.')

                target_output = project_root / ".ai_transcripts"
                
                if transcript_str and os.path.exists(transcript_str):
                    transcript_path = Path(transcript_str)
                else:
                    transcript_path = DEFAULT_APP_DATA / "brain" / conversation_id / ".system_generated" / "logs" / "transcript.jsonl"
                
                run_archiver(transcript_path, target_output, conversation_id, project_root.name)
        except Exception as e:
            # Hooks should never crash the agent loop
            sys.stderr.write(f"[archiver hook warning] {e}\n")
        
        # Stop hook contract requires JSON response
        sys.stdout.write(json.dumps({"decision": "allow"}))
        return

    # 2. CLI Invocation (bypasses stdin completely)
    target_output = Path(args.output_dir)
    
    if args.transcript_path:
        transcript_path = Path(args.transcript_path)
        conv_id = args.conversation_id or "session"
    elif args.conversation_id:
        conv_id = args.conversation_id
        transcript_path = DEFAULT_APP_DATA / "brain" / conv_id / ".system_generated" / "logs" / "transcript.jsonl"
    else:
        print("[!] Either --transcript-path or --conversation-id must be provided, or run with --hook.")
        sys.exit(1)

    run_archiver(transcript_path, target_output, conv_id, args.project_name)

if __name__ == "__main__":
    main()
