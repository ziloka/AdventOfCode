const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

// parse string
const answers = getInput().split("\n\n").map((group) => group.split("\n").map((s) => s.split("")));

console.time();
console.log(`part 1: ${answers.map((group) => [...new Set(group.flat())].length).reduce((a, b) => a + b)}`);
console.log(`part 2: ${getInput().split('\n\n').map(s => ((n = s.split('\n').length), (Array.prototype.reduce.bind(s, (a, c) => a + ((s.split(c).length - 1) === n), 0)() / n))).reduce((a, c) => a + c, 0)}`);
console.timeEnd();