const fs = require('fs');
const path = require('path');

const land = require('./doctrines_land.js');
const naval = require('./doctrines_naval.js');
const ui = require('./doctrines_ui.js');
const sf = require('./doctrines_sf.js');
const air = require('./doctrines_air.js');

const dict = Object.assign({}, land, naval, ui, sf, air);

const srcPath = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/doctrines_l_english.yml';
const destPathApp = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/doctrines_l_braz_por.yml';
const destPathMod = path.join(__dirname, '../localisation/braz_por/doctrines_l_braz_por.yml');

const content = fs.readFileSync(srcPath, 'utf8');
const lines = content.split(/\r?\n/);

let replacedCount = 0;
let unchangedVarCount = 0;
let untouchedLines = 0;

const outLines = lines.map((line, idx) => {
  if (idx === 0) {
    return 'l_braz_por:';
  }
  if (!line.trim()) {
    untouchedLines++;
    return line;
  }
  
  // Match key:number "value" # comment
  // Example:  GRAND_DOCTRINE_MOBILE_WARFARE: "Mobile Warfare"
  const colonIndex = line.indexOf(':');
  if (colonIndex === -1) {
    untouchedLines++;
    return line;
  }
  
  const beforeColon = line.substring(0, colonIndex);
  const afterColon = line.substring(colonIndex + 1);
  const key = beforeColon.trim();
  
  // Find first quote and last quote
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
    // If it is a variable pointer like "$foo$", leave it as original
    unchangedVarCount++;
    return line;
  }
});

const finalContent = '\ufeff' + outLines.join('\n');

// Write to both paths
fs.writeFileSync(destPathApp, finalContent, 'utf8');
fs.writeFileSync(destPathMod, finalContent, 'utf8');

console.log('Build completed!');
console.log('Total lines:', outLines.length);
console.log('Replaced translated keys:', replacedCount);
console.log('Unchanged variable keys:', unchangedVarCount);
console.log('Untouched lines (empty/header):', untouchedLines);
