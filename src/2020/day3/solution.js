const arr = require('fs').readFileSync('./input.txt', 'utf8').split("\n").map((s) => s.trim()); /// split, and trim space

function numTreeEncounters(slope) {
  let result = 0;
  let previousXValue = 0;
  for (let i = slope.y; i < arr.length; i++) {
    let str = arr[i];
    previousXValue += slope.x;
    if (previousXValue >= str.length) {
      let temp = "";
      for (let i = 0; i <= Math.ceil(previousXValue / str.length); i++) {
        temp += str;
      }
      str = temp;
    }
    if (str.charAt(previousXValue) == "#") {
      result++;
    }
  }
  return result;
}

function part1() {
  return numTreeEncounters({ x: 3, y: 1 });
}

function part2() {
  return [{x: 1, y: 1}, {x: 3, y: 1}, {x: 5, y: 1}, {x: 7, y: 1}, {x: 1, y: 2}].map((o) => numTreeEncounters(o)).reduce((a, b) => a * b, 1);
}


console.time();
// console.log(`part 1: ${part1()}`);
// console.log(`part 2: ${part2()}`);
console.log(numTreeEncounters({x: 1, y: 2}));
console.timeEnd();