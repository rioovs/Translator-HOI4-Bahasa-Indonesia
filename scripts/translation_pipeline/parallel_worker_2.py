# -*- coding: utf-8 -*-
"""
parallel_worker_2.py - Regional Decisions, Factions, Triggers & Goals Worker
"""
import sys
import os
import time

sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")
from universal_dlc_translator import process_file

FILES = [
    "bba_decisions",
    "aat_decisions",
    "SEA_decisions",
    "TAOG_decisions",
    "goe_decisions",
    "toa_decisions",
    "lar_decisions",
    "mun_decisions",
    "wtt_political_power_struggle",
    "wtt_ss_recruitment",
    "wtt_border_conflict",
    "factions",
    "triggers",
    "goals",
]

def main():
    print(f"[WORKER 2] Starting {len(FILES)} files...", flush=True)
    start = time.time()
    for idx, f in enumerate(FILES, 1):
        print(f"\n[WORKER 2 - {idx}/{len(FILES)}] STARTING: {f}", flush=True)
        try:
            process_file(f)
        except Exception as e:
            print(f"[ERROR W2] {f}: {e}", flush=True)
        time.sleep(0.5)
    print(f"\n[WORKER 2] COMPLETED in {(time.time()-start)/60:.1f}m", flush=True)

if __name__ == "__main__":
    main()
