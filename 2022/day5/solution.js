const input = require('fs').readFileSync('input.txt', 'utf8');

const parseInput = (rawInput) => {
  let crateRows = rawInput.split("\n\n")[0].split('\n')
  let numStacks = (crateRows[0].length + 1) / 4;
  let stacks = new Array(numStacks + 1).fill().map(() => []);

  for (let row of rawInput.split("\n\n")[0].split('\n')) {
    if (row[1] === '1') break;

    for (let i = 0; i < numStacks; i++) {
      let crate = row[4 * i + 1];
      if (crate !== ' ') {
        stacks[i + 1].push(crate);
      }
    }
  }

  let instructions = rawInput.split("\n\n")[1].split('\n').map(line => {
    let [ amount, from, to ] = line.match(/\d+/g).map((d) => +d);
    return { amount, from, to };
  });

  return { instructions, stacks };
}

function part1(stacks, instructions) {
  instructions.forEach((instruction) => {
    Array.from({ length: instruction.amount }, () => {
      stacks[instruction.to].unshift(stacks[instruction.from].shift());
    });
  });
  return stacks.filter((s) => s.length > 0).reduce((a, b) => a + b[0], "");
}

function part2(stacks, instructions) {
  instructions.forEach((instruction) => {
    stacks[instruction.to].unshift(...stacks[instruction.from].splice(0, instruction.amount));
  });
  return stacks.filter((s) => s.length > 0).reduce((a, b) => a + b[0], "");
}

// DEEP CLONE VALUES (structuredClone method or JSON.parse(JSON.stringify(data))) because arrays are passed by reference *
const { stacks, instructions } = parseInput(input);
console.time();
console.log(`part 1: ${part1(JSON.parse(JSON.stringify(stacks)), instructions)}`);
console.log(`part 2: ${part2(JSON.parse(JSON.stringify(stacks)), instructions)}`);
console.timeEnd();