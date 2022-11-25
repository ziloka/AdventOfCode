function getInput() {
  return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr) {
  let result = 0;
  for (let e1 of arr) {
    for (let e2 of arr) {
      if (e1 + e2 == 2020) {
        result = e1 * e2;
        break;
      }
    }
  }
  return result;
}

function part2(arr) {
  let result = 0;
  for (let e1 of arr) {
    for (let e2 of arr) {
      for (let e3 of arr) {
        if (e1 + e2 + e3 == 2020) {
          result = e1 * e2 * e3;
          break;
        }
      }
    }
  }
  return result;
}

const arr = getInput().split("\n").map((s) => +s.trim()); /// split, and convert strings into numbers
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();