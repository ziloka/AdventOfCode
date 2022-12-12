let input = require('fs').readFileSync('input.txt', 'utf8');

function parse(str) {
  return str
    .replace(/\r\n/g, '\n')
    .split('\n\n')
    .map((m) => m.split('\n'))
    .map(m => {
      let monkey = { "monkeyBusiness": 0 };

      ["id","items","op","tst","iftrue","iffalse"].map((test, idx) => {
        let val = m[idx].trim();
        switch (test) {
          case "id":
          case "iftrue":
          case "iffalse":
            val = Number(val.replace(/[^\d]/g, ''));
          break;
          case "items":
            val = val.split(':')[1].split(', ').map(Number);
            monkey["worryLevel"] = val[0];
            break;
          case "op":
            val = eval(`(num) => { return ${val.split('= ')[1].replace(/new|old/g, "num")}; }`);
          break;
          case "tst":
            let t = Number(val.split("divisible by ")[1]);
            monkey["divby"] = t;
            val = (line) => { return line % t === 0 };
          break;
        }
        monkey[test] = val;
      });
      return monkey;
  });
};

function solution (monkeys, maxrounds = 20) {
  let getWorryLevel = (worryLevel) => maxrounds == 20
    ? Math.floor(worryLevel / 3)
    : worryLevel % monkeys.reduce((a, b) => a * b.divby, 1);
  for (let round = 1; round <= maxrounds; round++) {
    for (let monkey of monkeys) {
      while (monkey.items.length !== 0) {
        let worryLevel = getWorryLevel(monkey.op(monkey.items.shift()));
        let destination = monkey.tst(worryLevel) ? monkey.iftrue : monkey.iffalse;
        monkeys[destination].items.push(worryLevel);
        monkey.monkeyBusiness++;
      }
    }
  }
  return monkeys
    .map(m => m.monkeyBusiness)
    .sort((a, b) => a - b)
    .slice(-2)
    .reduce((a, b) => a * b, 1);
}

console.time();
let part1 = solution(parse(input), 20);
let part2 = solution(parse(input), 10000);
console.log(part1);
console.log(part2);
console.timeEnd();
