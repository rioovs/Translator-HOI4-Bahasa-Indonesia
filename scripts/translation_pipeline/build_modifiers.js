const fs = require('fs');
const path = require('path');

const p1 = require('./modifiers_part1.js');
const p2 = require('./modifiers_part2.js');
const p3 = require('./modifiers_part3.js');
const p4 = require('./modifiers_part4.js');
const p5 = require('./modifiers_part5.js');

const dict = Object.assign({}, p1, p2, p3, p4, p5);

const srcPath = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/modifiers_l_english.yml';
const destPathApp = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/modifiers_l_braz_por.yml';
const destPathMod = path.join(__dirname, '../localisation/braz_por/modifiers_l_braz_por.yml');

const content = fs.readFileSync(srcPath, 'utf8');
const lines = content.split(/\r?\n/);

let replacedCount = 0;
let preservedCount = 0;
let untouchedLines = 0;

const outLines = lines.map((line, idx) => {
  if (idx === 0) {
    return 'l_braz_por:';
  }
  if (!line.trim() || line.trim().startsWith('#')) {
    untouchedLines++;
    return line;
  }
  
  // Handle line 2628 special anomaly in Paradox file
  // cannot_retreat_while_attacking_tt: " $MODIFIER_CANNOT_RETREAT_WHILE_ATTACKING$: $RIGHT|+0$" local_resource_gain_efficiency_per_infrastructure_tt: " $MODIFIER_LOCAL_RESOURCE_GAIN_EFFICIENCY_PER_INFRASTRUCTURE$: $RIGHT|+=%1$"
  if (line.includes('cannot_retreat_while_attacking_tt') && line.includes('local_resource_gain_efficiency_per_infrastructure_tt')) {
    preservedCount++;
    return line;
  }
  
  const colonIndex = line.indexOf(':');
  if (colonIndex === -1) {
    untouchedLines++;
    return line;
  }
  
  const beforeColon = line.substring(0, colonIndex);
  const afterColon = line.substring(colonIndex + 1);
  const key = beforeColon.trim();
  
  const firstQuote = afterColon.indexOf('"');
  const lastQuote = afterColon.lastIndexOf('"');
  
  if (firstQuote === -1 || lastQuote === -1 || firstQuote === lastQuote) {
    untouchedLines++;
    return line;
  }
  
  const prefix = beforeColon + ':' + afterColon.substring(0, firstQuote + 1);
  const originalVal = afterColon.substring(firstQuote + 1, lastQuote);
  const suffix = afterColon.substring(lastQuote);
  
  if (dict.hasOwnProperty(key)) {
    replacedCount++;
    return prefix + dict[key] + suffix;
  } else {
    preservedCount++;
    return line;
  }
});

const finalContent = '\ufeff' + outLines.join('\n');

// Ensure directories exist
fs.mkdirSync(path.dirname(destPathApp), { recursive: true });
fs.mkdirSync(path.dirname(destPathMod), { recursive: true });

// Write to both paths with UTF-8 BOM
fs.writeFileSync(destPathApp, finalContent, 'utf8');
fs.writeFileSync(destPathMod, finalContent, 'utf8');

console.log('Build completed successfully!');
console.log('Total lines:', outLines.length);
console.log('Replaced translated keys:', replacedCount);
console.log('Preserved keys (vars/formulas/icons):', preservedCount);
console.log('Untouched lines (header/empty/comments):', untouchedLines);
