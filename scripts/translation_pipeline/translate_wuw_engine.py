# -*- coding: utf-8 -*-
import json
import re
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

TERMS_MAP = [
    (r'\bFour[- ]Year Plan\b', 'Rencana Empat Tahun'),
    (r'\bInner Circle\b', 'Lingkaran Dalam'),
    (r'\bMEFO [Bb]ills?\b', 'Surat Utang MEFO'),
    (r'\btagihan MEFO\b', 'Surat Utang MEFO'),
    (r'\bSpecial Projects?\b', 'Proyek Khusus'),
    (r'\bproyek khusus\b', 'Proyek Khusus'),
    (r'\bGeneral Staff\b', 'Staf Umum'),
    (r'\bstaf umum\b', 'Staf Umum'),
    (r'\bDanubian Federation\b', 'Federasi Donau'),
    (r'\bDanubian\b', 'Donau'),
    (r'\bDual Monarchy\b', 'Monarki Ganda'),
    (r'\bmonarki ganda\b', 'Monarki Ganda'),
    (r'\bNational Focus\b', 'Fokus Nasional'),
    (r'\bfokus nasional\b', 'Fokus Nasional'),
    (r'\bCivilian Factor(?:y|ies)\b', 'Pabrik Sipil'),
    (r'\bpabrik sipil\b', 'Pabrik Sipil'),
    (r'\bMilitary Factor(?:y|ies)\b', 'Pabrik Militer'),
    (r'\bpabrik militer\b', 'Pabrik Militer'),
    (r'\bNaval Dockyards?\b', 'Galangan Kapal Angkatan Laut'),
    (r'\bgalangan kapal angkatan laut\b', 'Galangan Kapal Angkatan Laut'),
    (r'\bSynthetic Refiner(?:y|ies)\b', 'Pabrik Pengilangan Sintetis'),
    (r'\bpabrik pengilangan sintetis\b', 'Pabrik Pengilangan Sintetis'),
    (r'\bFuel Silos?\b', 'Silo Bahan Bakar'),
    (r'\bsilo bahan bakar\b', 'Silo Bahan Bakar'),
    (r'\bAir Bases?\b', 'Pangkalan Udara'),
    (r'\bpangkalan udara\b', 'Pangkalan Udara'),
    (r'\bResearch Slots?\b', 'Slot Riset'),
    (r'\bslot riset\b', 'Slot Riset'),
    (r'\bWorld Tension\b', 'Ketegangan Dunia'),
    (r'\bketegangan dunia\b', 'Ketegangan Dunia'),
    (r'\bWar Support\b', 'Dukungan Perang'),
    (r'\bdukungan perang\b', 'Dukungan Perang'),
    (r'\bPolitical Power\b', 'Kekuasaan Politik'),
    (r'\bkekuasaan politik\b', 'Kekuasaan Politik'),
    (r'\bConsumer Goods\b', 'Barang Konsumsi'),
    (r'\bbarang konsumsi\b', 'Barang Konsumsi'),
    (r'\bCivil War\b', 'Perang Saudara'),
    (r'\bperang saudara\b', 'Perang Saudara'),
    (r'\bNon-Aggression Pact\b', 'Pakta Non-Agresi'),
    (r'\bpakta non-agresi\b', 'Pakta Non-Agresi'),
    (r'\bMutual Defense Pact\b', 'Pakta Pertahanan Bersama'),
    (r'\bpakta pertahanan bersama\b', 'Pakta Pertahanan Bersama'),
    (r'\bPuppet state\b', 'Negara Boneka'),
    (r'\bpuppet state\b', 'Negara Boneka'),
    (r'\bIndivisible and Inseparable\b', 'Tak Terpisahkan dan Tak Terbagi'),
    (r'\bkerja sama\b', 'kerja sama'),
    (r'\bkerjasama\b', 'kerja sama'),
    (r'\bKerjasama\b', 'Kerja Sama'),
]

def mask_text(text):
    tokens = []
    # Token regex: escaped newlines, escaped quotes, script blocks, variables, color tags, texticons
    pattern = re.compile(
        r'(\\n)|(\\")|(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)'
    )
    def repl(m):
        tok = m.group(0)
        idx = len(tokens)
        tokens.append(tok)
        return f"___TK{idx}___"
    masked = pattern.sub(repl, text)
    return masked, tokens

def unmask_text(text, tokens):
    res = text
    for i, tok in enumerate(tokens):
        # In translation, Google sometimes introduces a space between ___TK and number or after it
        # Handle ___TK{i}___ with optional spaces within or around placeholder
        ph = f"___TK{i}___"
        res = re.sub(r'___\s*TK\s*' + str(i) + r'\s*___', tok, res)
        
    # Space formatting for color tags
    res = re.sub(r'§([A-Za-z])\s+', r'§\1', res)
    res = re.sub(r'\s+§!', '§!', res)
    res = re.sub(r'\[\s+', '[', res)
    res = re.sub(r'\s+\]', ']', res)
    res = re.sub(r'([a-zA-Z0-9])§([A-Za-z])', r'\1 §\2', res)
    res = re.sub(r'§!\s*([a-zA-Z0-9])', r'§! \1', res)
    res = re.sub(r'\s*\\n\s*', r'\\n', res)
    
    # Internal quote safety: ensure quotes inside string are escaped
    res = res.replace('“', '\\"').replace('”', '\\"')
    res = re.sub(r'(?<!\\)"', r'\"', res)
    
    # Apply terminology
    for pat, rep in TERMS_MAP:
        res = re.sub(pat, rep, res)
        
    # Clean up double spaces
    res = re.sub(r'[ \t]+', ' ', res).strip()
    return res

def translate_single_val(val):
    val_stripped = val.strip()
    if not val_stripped:
        return val
    if re.match(r'^\$[A-Za-z0-9_.-]+\$$', val_stripped):
        return val
        
    masked, tokens = mask_text(val)
    
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_tr = ''.join([p[0] for p in data[0] if p[0]])
                return unmask_text(raw_tr, tokens)
        except Exception as e:
            if attempt == 3:
                print(f"Error after 4 attempts for: {val[:40]}...: {e}")
                return unmask_text(masked, tokens)
            time.sleep(1 + attempt)

if __name__ == '__main__':
    test_cases = [
        "Indivisible and Inseparable",
        "Activates the §YInner Circle§! Mechanic.\\n\\n",
        "The Four-Year Plan",
        "Completing this focus will §Rlock§! §Y$FOCUS_1$§! and §Y$FOCUS_2$§! for their respective $GER_inner_circle_member_title$s",
        "$GER_autobahn_desc$",
        "§Y$CHARACTER$§! is working on this focus. \\nProgress: §Y$FLAG_DAYS$§!/[?temp_focus_days] days",
        "Establish Beneficial Weapons Contracts",
        "Is either §Y[AUS.GetNameDef]§! or §Y[HUN.GetNameDef]§! and has any §YAustro-Hungarian Contingent State§! as their subject."
    ]
    for tc in test_cases:
        res = translate_single_val(tc)
        print(f"ORIG: {tc}")
        print(f"RES:  {res}\n")
