let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
var n = input;
console.log(n[0] + " + " + n[1] + " = " + String(parseInt(n[0])+parseInt(n[1])))