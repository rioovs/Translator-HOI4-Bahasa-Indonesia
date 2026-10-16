# -*- coding: utf-8 -*-
import os
import glob

files = glob.glob(r"f:\New Coding\rea-hoi4-indonesia\scripts\*taog*.py")
for f in files:
    print(f"{os.path.basename(f)} : {os.path.getsize(f)} bytes")
