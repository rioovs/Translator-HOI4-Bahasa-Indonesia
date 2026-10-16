import json

with open('scripts/taog_events_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

part1_keys = []
part2_keys = []
part3_keys = []

for item in items:
    k = item['key']
    fam = k.split('.')[0]
    if fam in ['taog_news', 'ABDA_events', 'ABDA_faction_membership_requirement_tt', 'ABDA_fortress_singapore_choice_tt',
                'INS_political_events', 'INS_chaos_events', 'INS_dutch_events', 'INS_industrial_events',
                'INS_industrial_events_5_desc_colonial', 'INS_industrial_events_5_desc_independent',
                'INS_industrial_events_5_t_colonial', 'INS_industrial_events_5_t_independent',
                'INS_exile_accepted_flag', 'INS_henri_winkelman_tt', 'INS_hey_btw_you_are_gonna_die_just_know_that_yeah_tt',
                'INS_peta_explain_tt', 'INS_peta_explain_tt_jap']:
        part1_keys.append(item)
    elif fam in ['INS_volksraad_events', 'INS_union_events', 'INS_communist_events', 'INS_limited_war_events', 'INS_martial_law_events']:
        part2_keys.append(item)
    elif fam in ['INS_loyalist_events', 'INS_revolution_events', 'INS_revolution_no_effect_tt']:
        part3_keys.append(item)
    else:
        print("Unassigned:", k)

print(f"Part 1: {len(part1_keys)} items")
print(f"Part 2: {len(part2_keys)} items")
print(f"Part 3: {len(part3_keys)} items")
print(f"Total: {len(part1_keys) + len(part2_keys) + len(part3_keys)} / {len(items)}")

with open('scripts/events_part1_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part1_keys, f, ensure_ascii=False, indent=2)
with open('scripts/events_part2_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part2_keys, f, ensure_ascii=False, indent=2)
with open('scripts/events_part3_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part3_keys, f, ensure_ascii=False, indent=2)
