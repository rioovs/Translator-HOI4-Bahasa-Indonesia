# -*- coding: utf-8 -*-
import json
import re

with open('chunks_5_6_7_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's write out translated pairs
# We'll build a dictionary mapping original English val to Indonesian translated text.
trans_dict = {}

def translate_desc(k, text):
    # Specialized translation logic for naval descriptions
    # Common patterns:
    # "The X Class battleships were..." -> "Kapal tempur Kelas X adalah..."
    # "The X class consisted of Y..." -> "Kelas X terdiri dari Y..."
    # "was a class of..." -> "adalah kelas..."
    # "built in..." -> "dibangun di..."
    # "armed with..." -> "dipersenjatai dengan..."
    
    # We will craft accurate translations per item or thematic group
    pass

