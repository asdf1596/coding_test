let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
var n = input[0];
var a = parseInt(n)%2==0 ? "even" : "odd"
console.log(n + " is "+a)