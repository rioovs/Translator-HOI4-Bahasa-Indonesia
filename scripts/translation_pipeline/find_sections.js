const fs = require('fs');
const src = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml';
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);

console.log('Total lines:', lines.length);
lines.forEach((l, i) => {
  if (l.trim().startsWith('#')) {
    console.log(`Line ${i + 1}: ${l.trim()}`);
  }
});
