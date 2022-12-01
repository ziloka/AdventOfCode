const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

// parse string into struct that is manipulatable
const boardingPasses = getInput().split("\n").map((code) => +getSeatId(code)).sort((a, b) => a - b);

function getSeatId(code) {
  const binarySpaceParition = (str, range, { lower, upper }) => {
    let rows = Array.from(Array(range + 1).keys());
    for (let s of str) {
      if (s == lower) rows = rows.slice(0, rows.length/2); // keep lower half
      else if (s == upper) rows = rows.slice(rows.length/2); // keep upper half
    }
    return rows[0];
  }
  const row = binarySpaceParition(code.slice(0, 7), 127, { lower: "F", upper: "B" });
  const column = binarySpaceParition(code.slice(7), 7, { lower: "L", upper: "R" });
  return  row * 8 + column;
}

console.time();
console.log(`part 1: ${boardingPasses[boardingPasses.length-1]}`);
console.log(`part 2: ${boardingPasses.find((value, index) => boardingPasses[0] + index != value)-1}`);
console.timeEnd();