# -*- coding: utf-8 -*-
import os
import json

subagents = {
    "b2ade33f": ("Decisions MEFO & Raids", r"C:\Users\riook\.gemini\antigravity\brain\b2ade33f-8c37-4fa1-a30a-f17b36f94325"),
    "2f44535e": ("Dutch East Indies & Indonesia", r"C:\Users\riook\.gemini\antigravity\brain\2f44535e-d384-4b76-8936-0e0318a51854"),
    "57ec85de": ("Countries & Cosmetic Names", r"C:\Users\riook\.gemini\antigravity\brain\57ec85de-f78a-4595-a5be-75e718de7767"),
    "18268706": ("Southeast Asia DLC", r"C:\Users\riook\.gemini\antigravity\brain\18268706-6ebb-4239-9b5a-cc4caec11af6")
}

for sid, (role, base_path) in subagents.items():
    tpath = os.path.join(base_path, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(tpath):
        continue
    with open(tpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    last_text = ""
    for l in reversed(lines):
        try:
            obj = json.loads(l)
            if obj.get("type") == "PLANNER_RESPONSE" and obj.get("content"):
                last_text = obj.get("content")
                break
        except Exception:
            pass
    print(f"==================================================")
    print(f"[{sid}] {role}:")
    print(last_text[-600:] if len(last_text) > 600 else last_text)
