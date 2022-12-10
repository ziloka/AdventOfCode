const input = require('fs').readFileSync('./input.txt', 'utf8').split("\n");

function getInstructionLifetime(instruction) {
  switch(instruction) {
    case "addx": return 2;
    case "noop": return 1;
  } 
}

function part1() {
  let result = 0, 
      x = 1,
      cycle = 1;
  for (let i = 0; i < input.length; i++) {
    let [instruction, value] = input[i].split(" "),
        lifetime = getInstructionLifetime(instruction);
    for (let j = 1; j <= lifetime; j++) {
      if (instruction == "addx" && lifetime == j) x += Number(value);
      cycle++;
      if (cycle % 40 == 20) result += cycle * x;
    }
  }
  return result;
}

function part2() {
  let x = 1, cycle = 1;
  let pixels = Array.from({ length: 6 }, () => Array.from({ length: 40 }, () => '.')); // make matrix with 6 rows, 40 columns, filled with '.'
  for (let i = 0; i < input.length; i++) {
    let [instruction, value] = input[i].split(" "),
        lifetime = getInstructionLifetime(instruction);
    for (let j = 1; j <= lifetime; j++) { // each cycle
      let row = Math.floor(cycle / 41), 
          column = (cycle - 1) % 40;
      // if (j == 1)
        // console.log(`Start cycle   ${cycle}: begin executing ${instruction} ${value ?? ''}`);
      
      // each cycle the crt draws
      // console.log(`During cycle  ${cycle}: CRT draws pixel in position ${column % 41}`);

      // if CRT position, the column, is in the range of the horizontal position (the x register)
      if ([x - 1, x, x + 1].includes(column)) pixels[row][column] = '#';
      
      // console.log(`Current CRT row: ${pixels[row].slice(0, column + 1).join('')}`);

      if (instruction == "addx" && lifetime == j) { // the end of the operation cycle
        x += Number(value);
        // console.log(`Ended cycle ${cycle}: finished executing ${input[i]} (Register X is now ${x}))`);
      }
      // console.log();
      
      cycle++;      
    }
  }
  return pixels.map(row => row.join('')).join('\n');
}

console.time();
console.log(part1());
console.log(part2());
console.timeEnd();