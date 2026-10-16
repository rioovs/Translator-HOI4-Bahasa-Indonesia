# -*- coding: utf-8 -*-
"""
batch_translate_dlc_queue.py
Sequentially translates the remaining 48 files (11,507 keys) into Indonesian:
- Events (base events, mtg, toa, lar, TAOG, tfv, mun, poland)
- Decisions (nsb, WUW, bba, aat, SEA, TAOG, goe, toa, lar, mun, wtt)
- Factions, Triggers, Goals
- Ideas & National Spirits
- Minor UI & System mechanics
"""
import sys
import os
import time

sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")
from universal_dlc_translator import process_file

QUEUE = [
    # 1. Events
    "events",
    "mtg_events",
    "toa_events",
    "lar_events",
    "TAOG_events",
    "tfv_events",
    "mun_events",
    "poland_dlc_events",

    # 2. Decisions & Mechanics
    "nsb_decisions",
    "WUW_decisions",
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

    # 3. Factions & Triggers & Goals
    "factions",
    "triggers",
    "goals",

    # 4. Ideas
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

    # 5. UI, Naval & System Mechanics
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
    "pdxonline"
]

def main():
    print(f"Starting Final Translation Queue of {len(QUEUE)} files...", flush=True)
    start_all = time.time()
    success = 0
    
    for idx, fname in enumerate(QUEUE, 1):
        print(f"\n[{idx}/{len(QUEUE)}] STARTING: {fname}", flush=True)
        try:
            ok = process_file(fname)
            if ok:
                success += 1
        except Exception as e:
            print(f"[ERROR] Failed processing {fname}: {e}", flush=True)
        time.sleep(0.3)
        
    elapsed = time.time() - start_all
    print(f"\n==========================================", flush=True)
    print(f"FINAL QUEUE COMPLETED: {success}/{len(QUEUE)} files in {elapsed/60:.1f} minutes", flush=True)
    print(f"==========================================", flush=True)

if __name__ == "__main__":
    main()
