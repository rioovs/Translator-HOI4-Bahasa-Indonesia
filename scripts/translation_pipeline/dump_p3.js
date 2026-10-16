const fs = require('fs');
const p3 = JSON.parse(fs.readFileSync('scripts/focus_part3_extracted.json', 'utf8'));

p3.forEach((x, idx) => {
  console.log(`[${idx}] ${x.key} :: ${x.val.replace(/\n/g, '\\n')}`);
});
