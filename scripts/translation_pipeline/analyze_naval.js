const fs = require('fs');

const p = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/equip_naval_l_english.yml';
const content = fs.readFileSync(p, 'utf8');
const lines = content.split(/\r?\n/);

const descs = [];
const countryKeys = [];
const genericHulls = [];
const otherKeys = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (i === 0 && line.trim().startsWith('l_english:')) continue;
  if (!line.trim() || line.trim().startsWith('#')) continue;

  const colonIdx = line.indexOf(':');
  if (colonIdx === -1) continue;
  const key = line.substring(0, colonIdx).trim();
  const firstQuote = line.indexOf('"', colonIdx);
  const lastQuote = line.lastIndexOf('"');
  if (firstQuote === -1 || lastQuote <= firstQuote) continue;
  const val = line.substring(firstQuote + 1, lastQuote);

  if (key.endsWith('_desc') || key.endsWith('_DESC')) {
    descs.push({ key, val });
  } else {
    const parts = key.split('_');
    if (parts[0].length === 3 && parts[0] === parts[0].toUpperCase()) {
      countryKeys.push({ key, val, tag: parts[0] });
    } else if (key.startsWith('ship_hull_')) {
      genericHulls.push({ key, val });
    } else {
      otherKeys.push({ key, val });
    }
  }
}

console.log('Total descriptions:', descs.length);
console.log('Total country keys:', countryKeys.length);
console.log('Total generic hull keys:', genericHulls.length);
console.log('Total other keys:', otherKeys.length);

const tags = new Set(countryKeys.map(x => x.tag));
console.log('Country tags (' + tags.size + '):', Array.from(tags).join(', '));

fs.writeFileSync('f:/New Coding/rea-hoi4-indonesia/naval_descs.json', JSON.stringify(descs, null, 2), 'utf8');
fs.writeFileSync('f:/New Coding/rea-hoi4-indonesia/naval_hulls.json', JSON.stringify(genericHulls, null, 2), 'utf8');
fs.writeFileSync('f:/New Coding/rea-hoi4-indonesia/naval_other.json', JSON.stringify(otherKeys, null, 2), 'utf8');
fs.writeFileSync('f:/New Coding/rea-hoi4-indonesia/naval_country.json', JSON.stringify(countryKeys, null, 2), 'utf8');
