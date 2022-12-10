const input = require('fs').readFileSync('./input.txt', 'utf8').split("\n").map((s) => s.split(" "));

function getInstructionLifetime(instruction) {
  switch(instruction) {
    case "addx": return 2;
    case "noop": return 1;
  }
}

function solution() {
  let part1 = 0,
      // make matrix with 6 rows, 40 columns, filled with '.'
      part2 = Array.from({ length: 6 }, () => Array.from({ length: 40 }, () => '.')),
      x = 1,
      cycle = 1;
  for (let i = 0; i < input.length; i++) {
    let [instruction, value] = input[i],
        lifetime = getInstructionLifetime(instruction);
    for (let j = 1; j <= lifetime; j++) { // for each cycle the instruction executed
      let row = Math.floor((cycle - 1) / 40),
          column = (cycle - 1) % 40;
      // if (j == 1)
      //   console.log(`Start cycle   ${cycle}: begin executing ${instruction} ${value ?? ''}`);

      // each cycle the crt draws
      // console.log(`During cycle  ${cycle}: CRT draws pixel in position ${column}`);

      // if CRT position, the column, is in the range of the horizontal position (the x register)
      if ([x - 1, x, x + 1].includes(column)) {
        part2[row][column] = '#';
      }

      // console.log(`Current CRT row: ${part2[row].slice(0, column + 1).join('')}`);

      if (instruction == "addx" && lifetime == j) { // the end of the cycle
        x += Number(value);
        // console.log(`Ended cycle ${cycle}: finished executing ${input[i]} (Register X is now ${x}))`);
      }
      // console.log();

      cycle++;

      // add up the signal strength
      if (cycle % 40 == 20) part1 += cycle * x;
    }
  }
  return [ part1, part2.map(row => row.join('')).join('\n') ];
}

console.time();
let [ part1, part2 ] = solution();
console.log(part1);
console.log(part2);
console.timeEnd();