# -*- coding: utf-8 -*-
"""
parallel_worker_1.py - Events & Major Decisions Worker
"""
import sys
import os
import time

sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")
from universal_dlc_translator import process_file

FILES = [
    "toa_events",
    "lar_events",
    "TAOG_events",
    "tfv_events",
    "mun_events",
    "poland_dlc_events",
    "nsb_decisions",
    "WUW_decisions",
]

def main():
    print(f"[WORKER 1] Starting {len(FILES)} files...", flush=True)
    start = time.time()
    for idx, f in enumerate(FILES, 1):
        print(f"\n[WORKER 1 - {idx}/{len(FILES)}] STARTING: {f}", flush=True)
        try:
            process_file(f)
        except Exception as e:
            print(f"[ERROR W1] {f}: {e}", flush=True)
        time.sleep(0.5)
    print(f"\n[WORKER 1] COMPLETED in {(time.time()-start)/60:.1f}m", flush=True)

if __name__ == "__main__":
    main()
