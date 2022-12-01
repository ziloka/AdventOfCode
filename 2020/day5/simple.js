const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

// parse string into struct that is manipulatable
const boardingPasses = getInput().split("\n").map((s) => parseInt(s.replace(/F|L/g, '0').replace(/B|R/g, '1'), 2)).sort((a, b) => a-b);

console.time();
console.log(`part 1: ${boardingPasses[boardingPasses.length-1]}`);
console.log(`part 2: ${boardingPasses.find((value, index) => boardingPasses[0] + index != value)-1}`);
console.timeEnd();