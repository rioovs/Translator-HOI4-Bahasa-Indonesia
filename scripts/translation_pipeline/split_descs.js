const descs = require('./naval_descs.json');

const genericDescs = [];
const countryDescs = [];

for (const d of descs) {
  const parts = d.key.split('_');
  if (parts[0].length === 3 && parts[0] === parts[0].toUpperCase()) {
    countryDescs.push(d);
  } else {
    genericDescs.push(d);
  }
}

console.log('Generic descs:', genericDescs.length);
console.log('Country descs:', countryDescs.length);

console.log('\n--- SAMPLE COUNTRY DESCS ---');
countryDescs.slice(0, 10).forEach(x => console.log(x.key + ':\n  ' + x.val.substring(0, 80) + '...'));
