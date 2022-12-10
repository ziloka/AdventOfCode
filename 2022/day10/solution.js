const input = require('fs').readFileSync('./input.txt', 'utf8').split("\n");

function takesXCycles(instruction) {
  switch(instruction) {
    case "addx": return 2;
    case "noop": return 1;
  } 
}

function part1() {
  let result = 0;
  let x = 1;
  let cycleNum = 1;
  for (let i = 0; i < input.length; i++) {
    let [instruction, value] = input[i].split(" ");
    for (let j = 1; j <= takesXCycles(instruction); j++) {
      if (instruction == "addx" && takesXCycles(instruction) == j) {
        x += Number(value);
      }
      cycleNum++;
      // get signal strength
      if (cycleNum % 40 == 20) {
        result += cycleNum * x;
      }
    }
  }
  return result;
}

function part2() {
  let x = 1;
  let cycleNum = 1;
  let pixels = Array.from({ length: 6 }, () => Array.from({ length: 40 }, () => '.')); // make 40 wide, 6 high, filled with '.'
  let row = 0;
  for (let i = 0; i < input.length; i++) {
    let [instruction, value] = input[i].split(" ");
    for (let j = 1; j <= takesXCycles(instruction); j++) { // each cycle

      let position = x, column = (cycleNum - 1) % 40;
      // if (j == 1)
        // console.log(`Start cycle   ${cycleNum}: begin executing ${instruction} ${value ?? ''}`);
      
      // each cycle the crt draws
      // console.log(`During cycle  ${cycleNum}: CRT draws pixel in position ${column % 41}`);

      if ([position - 1, position, position + 1].includes(column)) { // where CRT is currently drawing
        pixels[row][column] = '#';
      } else {
        pixels[row][column] = '.';
      }
      // console.log(`Current CRT row: ${pixels[row].slice(0, column + 1).join('')}`);

      if (instruction == "addx" && takesXCycles(instruction) == j) { // the end of the operation cycle
        x += Number(value);
        // console.log(`Ended cycle ${cycleNum}: finished executing ${input[i]} (Register X is now ${x}))`);
      }
      // console.log();
      
      cycleNum++;
       // change row to modify
      if (cycleNum % 41 == 0) row++;
      
    }
  }
  return pixels.map(row => row.join('')).join('\n');
}

console.log(part1());
console.log(part2());