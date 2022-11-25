const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

// parse string into struct that is manipulatable
const boardingPasses = getInput().split("\n").map((code) => +getSeatId(code)).sort((a, b) => a - b);

function getSeatId(code) {
  // determine what row you sit in
  let rows = Array.from(Array(127 + 1).keys()); // keep the number even
  for (let gravity of code.slice(0, 7)) { // F or B
    if (gravity == "F") {
      // keep the lower half
      rows = rows.slice(0, rows.length/2);
    } else if(gravity == "B") {
      // keep the upper half
      rows = rows.slice(rowNums.length/2);
    }
  }

  // determine what column you sit in
  let columns = Array.from(Array(7 + 1).keys()); // keep the number even
  for (let shift of code.slice(7)) { // L or R
    if (shift == "L") {
      // keep lower half
      columns = columns.slice(0, columns.length/2);
    } else if(shift == "R") {
      // keep the upper half
      columns = columns.slice(columns.length/2);
    }
  }

  return  rowNums[0] * 8 + columns[0];
}

console.time();
console.log(`part 1: ${boardingPasses[boardingPasses.length-1]}`);
console.log(`part 2: ${boardingPasses.find((value, index) => boardingPasses[0] + index != value)-1}`);
console.timeEnd();