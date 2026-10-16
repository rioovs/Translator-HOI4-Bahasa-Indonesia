# -*- coding: utf-8 -*-
"""
parallel_worker_3.py - Ideas, Naval Equip & System Mechanics Worker
"""
import sys
import os
import time

sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")
from universal_dlc_translator import process_file

FILES = [
    "WUW_ideas",
    "nsb_ideas",
    "toa_ideas",
    "aat_ideas",
    "goe_ideas",
    "TAOG_ideas",
    "bba_ideas",
    "mtg_ideas",
    "mun_ideas",
    "wtt_ideas",
    "bba_bop",
    "equip_naval",
    "achievements",
    "career_profile_more_customization",
    "career_profile_achievements",
    "technology_sharing",
    "collections",
    "logistics",
    "multiplayer",
    "government_in_exile",
    "navy",
    "state",
    "subscription",
    "pdxonline",
]

def main():
    print(f"[WORKER 3] Starting {len(FILES)} files...", flush=True)
    start = time.time()
    for idx, f in enumerate(FILES, 1):
        print(f"\n[WORKER 3 - {idx}/{len(FILES)}] STARTING: {f}", flush=True)
        try:
            process_file(f)
        except Exception as e:
            print(f"[ERROR W3] {f}: {e}", flush=True)
        time.sleep(0.5)
    print(f"\n[WORKER 3] COMPLETED in {(time.time()-start)/60:.1f}m", flush=True)

if __name__ == "__main__":
    main()
