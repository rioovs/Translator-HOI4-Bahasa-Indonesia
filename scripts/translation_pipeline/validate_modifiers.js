const fs = require('fs');
const path = require('path');

const srcPath = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/modifiers_l_english.yml';
const destPathApp = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/modifiers_l_braz_por.yml';
const destPathMod = path.join(__dirname, '../localisation/braz_por/modifiers_l_braz_por.yml');

function validateFile(filePath, label) {
  console.log(`\n=== Validating ${label}: ${filePath} ===`);
  const buf = fs.readFileSync(filePath);
  
  // Check BOM
  if (buf[0] === 0xef && buf[1] === 0xbb && buf[2] === 0xbf) {
    console.log('✓ UTF-8 BOM present');
  } else {
    console.error('✗ UTF-8 BOM missing!');
    process.exit(1);
  }
  
  const text = buf.toString('utf8').replace(/^\ufeff/, '');
  const lines = text.split(/\r?\n/);
  console.log(`Line count: ${lines.length}`);
  
  if (lines[0] !== 'l_braz_por:') {
    console.error(`✗ First line is not l_braz_por:, got: "${lines[0]}"`);
    process.exit(1);
  } else {
    console.log('✓ Header is l_braz_por:');
  }
  
  return lines;
}

const srcLines = fs.readFileSync(srcPath, 'utf8').replace(/^\ufeff/, '').split(/\r?\n/);
const appLines = validateFile(destPathApp, 'App File');
const modLines = validateFile(destPathMod, 'Mod File');

if (appLines.length !== srcLines.length) {
  console.error(`✗ Line count mismatch: src ${srcLines.length} vs dest ${appLines.length}`);
  process.exit(1);
} else {
  console.log('✓ Line count matches source (2630 lines)');
}

let varErrors = 0;
let iconErrors = 0;
let colorErrors = 0;
let keyErrors = 0;

for (let i = 0; i < srcLines.length; i++) {
  const src = srcLines[i];
  const dest = appLines[i];
  
  if (i === 0) continue;
  if (!src.trim() || src.trim().startsWith('#')) continue;
  
  // Check key match
  const colonSrc = src.indexOf(':');
  const colonDest = dest.indexOf(':');
  const srcKey = colonSrc !== -1 ? src.substring(0, colonSrc).trim() : '';
  const destKey = colonDest !== -1 ? dest.substring(0, colonDest).trim() : '';
  if (srcKey !== destKey) {
    console.error(`Line ${i+1}: key mismatch "${srcKey}" vs "${destKey}"`);
    keyErrors++;
  }
  
  // Extract variables $...$
  const srcVars = (src.match(/\$[^$]+\$/g) || []).sort();
  const destVars = (dest.match(/\$[^$]+\$/g) || []).sort();
  if (JSON.stringify(srcVars) !== JSON.stringify(destVars)) {
    console.error(`Line ${i+1} [${srcKey}] Variable mismatch:`);
    console.error('  src :', srcVars);
    console.error('  dest:', destVars);
    varErrors++;
  }
  
  // Extract icons £...£ or £... followed by space/closing paren
  const srcIcons = (src.match(/£[a-zA-Z0-9_]+(?:\|[0-9]+)?(?:£|(?=[\s\)]))/g) || []).sort();
  const destIcons = (dest.match(/£[a-zA-Z0-9_]+(?:\|[0-9]+)?(?:£|(?=[\s\)]))/g) || []).sort();
  if (JSON.stringify(srcIcons) !== JSON.stringify(destIcons)) {
    console.error(`Line ${i+1} [${srcKey}] Icon mismatch:`);
    console.error('  src :', srcIcons);
    console.error('  dest:', destIcons);
    iconErrors++;
  }
  
  // Extract color codes §. and §!
  const srcColors = (src.match(/§./g) || []).sort();
  const destColors = (dest.match(/§./g) || []).sort();
  if (JSON.stringify(srcColors) !== JSON.stringify(destColors)) {
    console.error(`Line ${i+1} [${srcKey}] Color code mismatch:`);
    console.error('  src :', srcColors);
    console.error('  dest:', destColors);
    colorErrors++;
  }
}

console.log('\n--- Validation Summary ---');
console.log(`Key errors: ${keyErrors}`);
console.log(`Variable errors: ${varErrors}`);
console.log(`Icon errors: ${iconErrors}`);
console.log(`Color code errors: ${colorErrors}`);

if (keyErrors === 0 && varErrors === 0 && iconErrors === 0 && colorErrors === 0) {
  console.log('\n🎉 ALL VALIDATIONS PASSED PERFECTLY!');
} else {
  console.error('\n❌ VALIDATION FAILED!');
  process.exit(1);
}
