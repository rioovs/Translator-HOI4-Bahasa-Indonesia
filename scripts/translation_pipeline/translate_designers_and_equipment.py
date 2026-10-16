# -*- coding: utf-8 -*-
"""
translate_designers_and_equipment.py
Translates equipment, designer, module, unit, doctrines, and combat files into Indonesian:
- designer
- plane_designer
- tank_modules
- ship_modules
- equipment
- POL_equipment
- unit
- unit_medals
- equip_naval
- doctrines
- combat
"""
import sys
import os
import time

sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")
from universal_dlc_translator import process_file

FILES = [
    "designer",
    "plane_designer",
    "tank_modules",
    "ship_modules",
    "combat",
    "unit",
    "unit_medals",
    "equip_naval",
    "doctrines",
    "equipment",
    "POL_equipment",
]

def main():
    print(f"Starting translation of {len(FILES)} designer & equipment files...", flush=True)
    start = time.time()
    success = 0
    for idx, fname in enumerate(FILES, 1):
        print(f"\n[{idx}/{len(FILES)}] PROCESSING: {fname}", flush=True)
        try:
            ok = process_file(fname)
            if ok:
                success += 1
        except Exception as e:
            print(f"[ERROR] Failed {fname}: {e}", flush=True)
        time.sleep(0.5)

    elapsed = time.time() - start
    print(f"\n==========================================", flush=True)
    print(f"COMPLETED {success}/{len(FILES)} designer/equipment files in {elapsed/60:.1f} minutes", flush=True)
    print(f"==========================================", flush=True)

if __name__ == "__main__":
    main()
