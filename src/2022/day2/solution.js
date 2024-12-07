const games = require('fs').readFileSync('input.txt', 'utf8').split('\n').map((s) => s.split(' '));

const theyChooseRock = 'A'; const theyChoosePaper = 'B'; const
  theyChooseScissors = 'C';
const meChooseRock = 'X'; const meChoosePaper = 'Y'; const
  meChooseScissors = 'Z';

const wins = [
  [theyChooseRock, meChoosePaper],
  [theyChoosePaper, meChooseScissors],
  [theyChooseScissors, meChooseRock],
];
const draws = [
  [theyChooseRock, meChooseRock],
  [theyChoosePaper, meChoosePaper],
  [theyChooseScissors, meChooseScissors],
];
const loses = [
  [theyChooseRock, meChooseScissors],
  [theyChoosePaper, meChooseRock],
  [theyChooseScissors, meChoosePaper]
];

function getPoints(strat, won, draw) {
  return (won ? 6 : draw ? 3 : 0) + (strat.charCodeAt(0) - 87);
}

function part1() {
  return games.reduce((currentPoints, round) => currentPoints + getPoints(round[1], wins.find((arr) => arr.every((e) => round.includes(e))), draws.find((arr) => arr.every((e) => round.includes(e)))), 0);
}

function part2() {
  const lose = 'X';
  const draw = 'Y';
  const win = 'Z';
  let points = 0;
  for (const round of games) {
    let outcomes = wins;
    if (round[1] == lose) outcomes = loses;
    else if (round[1] == draw) outcomes = draws;
    points += getPoints(outcomes.find((arr) => arr[0] == round[0])[1], round[1] == win, round[1] == draw);
  }
  return points;
}

const start = process.hrtime.bigint();
console.log(`part 1: ${part1()}`);
console.log(`part 2: ${part2()}`);
console.log(`took: ${(process.hrtime.bigint() - start) / 1_000_000n}ms`);
