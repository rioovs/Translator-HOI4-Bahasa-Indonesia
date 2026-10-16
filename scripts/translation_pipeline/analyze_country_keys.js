const countryKeys = require('./naval_country.json');

console.log('Total country keys:', countryKeys.length);

const classNames = [];
const otherNames = [];

for (const item of countryKeys) {
  if (item.val.includes('Class') || item.val.includes('class')) {
    classNames.push(item);
  } else {
    otherNames.push(item);
  }
}

console.log('Keys with Class/class:', classNames.length);
console.log('Keys without Class/class:', otherNames.length);

console.log('\n--- SAMPLE OTHER NAMES (without Class) ---');
otherNames.slice(0, 30).forEach(x => console.log(`${x.key}: "${x.val}"`));
