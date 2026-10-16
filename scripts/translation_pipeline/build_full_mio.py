# -*- coding: utf-8 -*-
import json
import re

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/military_industrial_organization_l_english.yml'
dst_game = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/military_industrial_organization_l_braz_por.yml'
dst_local = 'f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/military_industrial_organization_l_braz_por.yml'

# Specific UI translations with escaped newlines \\n
ui_map = {
    "mio_sorting_name": "Nama",
    "mio_sorting_task_capacity": "Kapasitas",
    "mio_sorting_task_cost": "Biaya",
    "INDUSTRIAL_ORG_LIST_WINDOW_TITLE": "Organisasi Industri Militer (MIO)",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_TITLE": "Rincian Organisasi",
    "INDUSTRIAL_ORG_OPEN_DETAILS_WINDOW": "Rincian",
    "INDUSTRIAL_ORG_OPEN_DETAILS_WINDOW_TOOLTIP": "Buka rincian Organisasi Industri Militer.",
    "INDUSTRIAL_ORG_OPEN_DETAILS_WINDOW_TOOLTIP_DELAYED": "$NAME|Y$ memiliki $NUMBER|Y0$ poin Sifat (Trait) untuk digunakan.",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_OPEN_QUEUE_BUTTON": "Antrean Sifat",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_SAVE_QUEUE_DESCRIPTION": "§HSimpan ke Berkas§!\\nSimpan antrean sifat ini ke berkas agar dapat diakses dalam permainan mendatang.",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_DELETE_QUEUE_DESCRIPTION": "§HHapus Antrean Tersimpan§!\\nKlik untuk mengosongkan antrean saat ini dan menghapus antrean tersimpan terpilih secara permanen.",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_DELETE_SPECIFIC_QUEUE_DESCRIPTION": "§HHapus Antrean Tersimpan§!\\n§RKlik untuk menghapus antrean sifat tersimpan secara permanen§!.",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_IMPORT_FROM_OTHER_MIO_TOOLTIP": "Impor sifat yang valid dari antrean sifat Organisasi Industri Militer lain: $ORG|Y$.",
    "INDUSTRIAL_ORG_QUEUE_WINDOW_INSTRUCTION": "Ketika Organisasi memiliki poin sifat, sifat pertama yang tersedia dalam antrean ini akan otomatis diselesaikan.\\n§GShift + Klik§! pada sifat untuk §Ymenambahkannya ke antrean§!.\\n§GSeret & Lepas§! untuk §Ymengubah urutan antrean§!.",
    "INDUSTRIAL_ORG_QUEUE_WINDOW_ITEM": "§GSelesai§!",
    "INDUSTRIAL_ORG_QUEUE_WINDOW_ITEM_DRAGDROP": "§GSeret & Lepas§! untuk mengubah urutan dalam antrean",
    "INDUSTRIAL_ORG_QUEUE_WINDOW_REMOVE_TOOLTIP": "Hapus dari Antrean",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_TRAITS_TAB": "Sifat (Traits)",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_TAB": "Riwayat",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_VARIANTS_HEADER": "Riwayat riset dan perancang",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_PRODUCTION_HEADER": "Riwayat lini produksi",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_OUTDATED_TOOLTIP": "§gPeralatan ini sudah usang.§!",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_NO_UPGRADE_TOOLTIP": "§gPeralatan ini sudah memiliki bonus dari sifat terbaru. Tidak perlu memperbarui varian.§!",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_UPGRADE_VARIANTS_TOOLTIP_CANT_AFFORD": "§RAnda tidak memiliki cukup Pengalaman untuk meningkatkan varian.§!",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_ENTRY_FLAVOR_RESEARCH_DATE": "Diteliti: $DATE$",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_ENTRY_FLAVOR_DESIGN_DATE": "Dirancang: $DATE$",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_ENTRY_FLAVOR_UNITS_PRODUCED": "Unit Diproduksi: $NUMBER|0H$",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_UPGRADE_VARIANTS_CONFIRM_POPUP_HEADER": "Tingkatkan dengan sifat terbaru",
    "INDUSTRIAL_ORG_DETAIL_WINDOW_HISTORY_UPGRADE_VARIANTS_CONFIRM_POPUP_DESC": "Apakah Anda yakin ingin meningkatkan $EQUIPMENT_NAME|Y$ dengan sifat terbaru?\\n\\nPeningkatan membutuhkan biaya $XPCOST|Y$.",
    "INDUSTRIAL_ORG_LIST_WINDOW_ASSIGN_TO_PROD_LINE_TOOLTIP": "§GKlik§! untuk §Ymenugaskan§! ke lini produksi ini",
    "INDUSTRIAL_ORG_LIST_WINDOW_ASSIGN_TO_SHIP_REFIT_TOOLTIP": "§GKlik§! untuk §Ymenugaskan§! ke perbaikan kapal",
    "INDUSTRIAL_ORG_LIST_WINDOW_ASSIGN_TO_VARIANT_TOOLTIP": "§GKlik§! untuk §Ymenugaskan§! ke varian peralatan ini",
    "INDUSTRIAL_ORG_LIST_WINDOW_ASSIGN_TO_RESEARCH_TOOLTIP": "§GKlik§! untuk §Ymenugaskan§! ke teknologi riset ini",
    "INDUSTRIAL_ORG_LIST_WINDOW_UNASSIGN_DESIGN_TEAM_TOOLTIP": "§GKlik§! untuk §Rmelepaskan penugasan§! dari rancangan ini",
    "INDUSTRIAL_ORG_LIST_WINDOW_UNASSIGN_MANUFACTURER_TOOLTIP": "§GKlik§! untuk §Rmelepaskan penugasan§! dari lini produksi ini",
    "INDUSTRIAL_ORG_LIST_WINDOW_FILTER_CATEGORY_TANK": "Tank",
    "INDUSTRIAL_ORG_LIST_WINDOW_FILTER_CATEGORY_SHIP": "Kapal",
    "INDUSTRIAL_ORG_LIST_WINDOW_FILTER_CATEGORY_PLANE": "Pesawat",
    "INDUSTRIAL_ORG_LIST_WINDOW_FILTER_CATEGORY_MATERIEL": "Material & Perlengkapan"
}

with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

out_lines = ['\ufeffl_braz_por:\n']

total_keys = 0
translated_keys = 0

for i in range(1, len(lines)):
    line = lines[i]
    stripped = line.strip()
    
    if not stripped or stripped.startswith('#'):
        out_lines.append(line)
        continue
        
    m = re.match(r'^(\s*)([A-Za-z0-9_-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
    if not m:
        out_lines.append(line)
        continue
        
    indent, key, version, val, comment = m.groups()
    ver_str = f":{version} " if version else ": "
    comment_str = comment if comment else ""
    total_keys += 1
    
    # Check if pure variable like "$NAME$" or "$equipment$"
    if re.match(r'^\$[A-Za-z0-9_]+\$$', val.strip()):
        out_lines.append(f"{indent}{key}{ver_str}\"{val}\"{comment_str}\n")
        continue
        
    new_val = val
    
    if key in ui_map:
        new_val = ui_map[key]
    else:
        # Pattern-based translation for MIO traits and descriptions
        t = val
        t = re.sub(r'\bProduction Line\b', 'Lini Produksi', t)
        t = re.sub(r'\bMass Production\b', 'Produksi Massal', t)
        t = re.sub(r'\bStandardized Parts\b', 'Komponen Terstandarisasi', t)
        t = re.sub(r'\bAssembly Line\b', 'Lini Perakitan', t)
        t = re.sub(r'\bQuality Control\b', 'Pengendalian Mutu', t)
        t = re.sub(r'\bArmor Plating\b', 'Pelat Lapis Baja', t)
        t = re.sub(r'\bCast Armor\b', 'Baja Tuang', t)
        t = re.sub(r'\bWelded Armor\b', 'Baja Las', t)
        t = re.sub(r'\bHigh-Velocity Gun\b', 'Meriam Kecepatan Tinggi', t)
        t = re.sub(r'\bHeavy Armament\b', 'Persenjataan Berat', t)
        t = re.sub(r'\bEngine Reliability\b', 'Keandalan Mesin', t)
        t = re.sub(r'\bAll-Weather Operations\b', 'Operasi Segala Cuaca', t)
        t = re.sub(r'\bLong Range Patrol\b', 'Patroli Jarak Jauh', t)
        t = re.sub(r'\bRapid Prototyping\b', 'Prototipe Cepat', t)
        t = re.sub(r'\bScientific Investment\b', 'Investasi Ilmiah', t)
        t = re.sub(r'\bSpecialized Design\b', 'Rancangan Khusus', t)
        t = re.sub(r'\bDepartment\b', 'Departemen', t)
        t = re.sub(r'\bPolicy\b', 'Kebijakan', t)
        t = re.sub(r'\bFunds\b', 'Dana', t)
        new_val = t
        
    if new_val != val:
        translated_keys += 1
        
    clean_val = new_val.replace('"', '\\"') if ('"' in new_val and '\\"' not in new_val) else new_val
    out_lines.append(f"{indent}{key}{ver_str}\"{clean_val}\"{comment_str}\n")

content = ''.join(out_lines)

with open(dst_game, 'w', encoding='utf-8') as f:
    f.write(content)
with open(dst_local, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated military_industrial_organization_l_braz_por.yml!")
print(f"Total lines: {len(out_lines)}")
print(f"Total keys: {total_keys}, Translated: {translated_keys}")
