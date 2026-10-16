const fs = require('fs');
const path = require('path');

const bDir = 'F:\\Apps\\Hearts_of_Iron_IV\\Hearts of Iron IV\\localisation\\braz_por';

const translatedList = [
  'core_l_braz_por.yml',
  'frontend_l_braz_por.yml',
  'topbar_l_braz_por.yml',
  'alerts_l_braz_por.yml',
  'country_l_braz_por.yml',
  'production_l_braz_por.yml',
  'trade_l_braz_por.yml',
  'deployment_l_braz_por.yml',
  'constructions_l_braz_por.yml',
  'peace_l_braz_por.yml',
  'waroverview_l_braz_por.yml',
  'war_l_braz_por.yml',
  'autonomy_l_braz_por.yml',
  'politics_l_braz_por.yml',
  'intel_ledger_l_braz_por.yml',
  'intelligence_agencies_l_braz_por.yml',
  'mapmode_l_braz_por.yml',
  'musicplayer_l_braz_por.yml',
  'loading_tips_l_braz_por.yml',
  'tactics_l_braz_por.yml',
  'theater_l_braz_por.yml',
  'ranks_l_braz_por.yml',
  'rules_l_braz_por.yml',
  'difficulty_l_braz_por.yml',
  'chat_l_braz_por.yml',
  'videos_l_braz_por.yml',
  'bookmarks_l_braz_por.yml',
  'parties_l_braz_por.yml',
  'game_rules_l_braz_por.yml',
  'doctrines_l_braz_por.yml',
  'combat_l_braz_por.yml',
  'diplomacy_l_braz_por.yml',
  'modifiers_l_braz_por.yml',
  'equipment_l_braz_por.yml',
  'traits_l_braz_por.yml',
  'equip_air_l_braz_por.yml',
  'ideas_l_braz_por.yml',
  'focus_l_braz_por.yml',
  'equip_naval_l_braz_por.yml',
  'military_industrial_organization_l_braz_por.yml',
  'events_l_braz_por.yml',
  'decisions_l_braz_por.yml',
  'operatives_l_braz_por.yml',
  'lar_operations_l_braz_por.yml',
  'ship_modules_l_braz_por.yml'
];

let totalTranslatedLines = 0;
let totalTranslatedKeys = 0;

for (const f of translatedList) {
  const p = path.join(bDir, f);
  if (fs.existsSync(p)) {
    const c = fs.readFileSync(p, 'utf8');
    const lines = c.split('\n');
    totalTranslatedLines += lines.length;
    const keys = lines.filter(l => /^\s*[A-Za-z0-9_.-]+:\d*\s*"/.test(l));
    totalTranslatedKeys += keys.length;
  }
}

console.log('Total translated files:', translatedList.length);
console.log('Total translated lines:', totalTranslatedLines);
console.log('Total translated keys:', totalTranslatedKeys);
