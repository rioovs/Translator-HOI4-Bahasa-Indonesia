# -*- coding: utf-8 -*-
"""
launch_10_workers.py
Launches 10 parallel worker processes to translate the final 36 files simultaneously.
"""
import sys
import os
import subprocess
import time

WORKER_GROUPS = [
    # Worker 0
    ["TAOG_decisions", "TAOG_ideas", "WUW_decisions"],
    # Worker 1
    ["nsb_decisions", "goe_decisions", "goe_ideas"],
    # Worker 2
    ["factions", "triggers", "goals", "lar_decisions"],
    # Worker 3
    ["toa_decisions", "mun_decisions", "mun_events", "mun_ideas"],
    # Worker 4
    ["tfv_events", "poland_dlc_events", "wtt_political_power_struggle", "wtt_ss_recruitment"],
    # Worker 5
    ["wtt_border_conflict", "wtt_ideas", "bba_ideas", "bba_bop"],
    # Worker 6
    ["mtg_ideas", "equip_naval", "achievements"],
    # Worker 7
    ["career_profile_achievements", "career_profile_more_customization", "technology_sharing", "collections"],
    # Worker 8
    ["logistics", "multiplayer", "government_in_exile", "navy"],
    # Worker 9
    ["state", "subscription", "pdxonline"],
]

def main():
    print(f"==================================================", flush=True)
    print(f"LAUNCHING 10 PARALLEL AGENTS FOR FINAL 36 FILES", flush=True)
    print(f"==================================================", flush=True)

    scripts_dir = r"f:\New Coding\rea-hoi4-indonesia\scripts"
    translator_script = os.path.join(scripts_dir, "universal_dlc_translator.py")
    python_exe = sys.executable

    processes = []
    start_time = time.time()

    for idx, group in enumerate(WORKER_GROUPS):
        cmd = [python_exe, translator_script] + group
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
        processes.append((idx, group, p))
        print(f"  [Agent {idx}] Started with {len(group)} files: {', '.join(group)}", flush=True)
        time.sleep(0.2)

    print("\nAll 10 agents running. Monitoring progress...\n", flush=True)

    # Wait for all processes to complete while streaming output
    finished = set()
    while len(finished) < len(processes):
        for idx, group, p in processes:
            if idx not in finished:
                ret = p.poll()
                if ret is not None:
                    finished.add(idx)
                    out, _ = p.communicate()
                    print(f"\n>>> [Agent {idx}] FINISHED (exit code {ret}) for {group}", flush=True)
                    # print last 5 lines of output
                    last_lines = [l for l in out.strip().splitlines() if l.strip()][-4:]
                    for ll in last_lines:
                        print(f"    [Agent {idx}]: {ll}", flush=True)
        time.sleep(0.5)

    elapsed = time.time() - start_time
    print(f"\n==================================================", flush=True)
    print(f"ALL 10 AGENTS COMPLETED in {elapsed:.1f} seconds!", flush=True)
    print(f"==================================================", flush=True)

if __name__ == "__main__":
    main()
