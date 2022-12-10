const input = require('fs').readFileSync('./input.txt', 'utf8').split("\n");

function getInstructionLifetime(command) {
  switch(command) {
    case "addx": return 2;
    case "noop": return 1;
  }
}

function solution() {
  let part1 = 0,
      // make matrix with 6 rows, 40 columns, filled with '.', which represents a dark pixel
      cathodeRayTube = Array.from({ length: 6 }, () => Array.from({ length: 40 }, () => '.')),
      x = 1,
      cycle = 1;
  input.forEach((instruction) => {
    const [command, value] = instruction.split(" "),
          lifetime = getInstructionLifetime(command);
    Array.from({ length: lifetime }, (_, i) => i + 1).forEach((age) => { // for each cycle the instruction executed
      const index = cycle - 1, 
          row = Math.trunc(index / 40),
          column = index % 40;

      // if (j == 1)
      //   console.log(`Start cycle   ${cycle}: begin executing ${instruction} ${value ?? ''}`);
      // console.log(`During cycle  ${cycle}: CRT draws pixel in position ${column}`);

      // if CRT position, the column, is in the range of the horizontal position (the x register), draw a lit pixel
      if ([x - 1, x, x + 1].includes(column)) cathodeRayTube[row][column] = '#';

      // console.log(`Current CRT row: ${cathodeRayTube[row].slice(0, column + 1).join('')}`);

      if (command == "addx" && lifetime == age) { // the end of the cycle
        x += Number(value);

        // console.log(`Ended cycle ${cycle}: finished executing ${input[i]} (Register X is now ${x}))`);
      }

      // console.log();

      cycle++;

      // add up the signal strength
      if (cycle % 40 == 20) part1 += cycle * x;
    });
  });
  return [ part1, cathodeRayTube.map(row => row.join('')).join('\n') ];
}

console.time();
let [ part1, part2 ] = solution();
console.log(part1);
console.log(part2);
console.timeEnd();