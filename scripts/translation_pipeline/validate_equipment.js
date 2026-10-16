const fs = require('fs');
const p = 'F:\\Apps\\Hearts_of_Iron_IV\\Hearts of Iron IV\\localisation\\braz_por\\equipment_l_braz_por.yml';
const content = fs.readFileSync(p, 'utf8');
const lines = content.split('\n');

let invalidLines = 0;
for (let i = 1; i < lines.length; i++) {
  const line = lines[i].trim();
  if (!line || line.startsWith('#')) continue;
  const match = line.match(/^([A-Za-z0-9_]+):(\d*)\s*"(.*)"$/);
  if (!match) {
    console.log(`Line ${i + 1}: ${line}`);
    invalidLines++;
    if (invalidLines > 5) break;
  }
}

if (invalidLines === 0) {
  console.log('PERFECT: All lines in equipment_l_braz_por.yml are valid Clausewitz YAML!');
}
