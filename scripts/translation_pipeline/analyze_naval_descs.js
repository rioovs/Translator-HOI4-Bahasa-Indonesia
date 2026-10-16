const descs = require('./naval_descs.json');

console.log('Total descs:', descs.length);

const varRefs = descs.filter(x => x.val.startsWith('$') && x.val.endsWith('$'));
console.log('Variable references (like $VAR$):', varRefs.length);

const nonVarDescs = descs.filter(x => !varRefs.includes(x));
console.log('Non-var descs:', nonVarDescs.length);

const uniqueVals = new Set(nonVarDescs.map(x => x.val));
console.log('Unique non-var desc texts:', uniqueVals.size);
