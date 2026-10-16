# -*- coding: utf-8 -*-
import os
import json

subagents = {
    "2f44535e": ("Dutch East Indies & Indonesia", r"C:\Users\riook\.gemini\antigravity\brain\2f44535e-d384-4b76-8936-0e0318a51854"),
    "57ec85de": ("Countries & Cosmetic Names", r"C:\Users\riook\.gemini\antigravity\brain\57ec85de-f78a-4595-a5be-75e718de7767")
}

for sid, (role, base_path) in subagents.items():
    tpath = os.path.join(base_path, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(tpath):
        continue
    with open(tpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    last_steps = lines[-4:]
    print(f"=== {role} ({sid}) ===")
    for l in last_steps:
        try:
            obj = json.loads(l)
            call_info = ""
            if obj.get("tool_calls"):
                call_info = f"-> {obj['tool_calls'][0].get('name')}: {obj['tool_calls'][0].get('args', {}).get('toolSummary', '')}"
            print(f"  Step {obj.get('step_index')}: {obj.get('type')} ({obj.get('status')}) {call_info}")
        except Exception as e:
            pass
