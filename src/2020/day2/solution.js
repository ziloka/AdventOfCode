function getInput() {
  // return `1-3 a: abcde
  // 1-3 b: cdefg
  // 2-9 c: ccccccccc`;
  return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr) {
  let result = 0; // how many valid passwords there are
  for (let [ passwordPolicy, passwd ] of arr.map((s) => s.split(":"))) {
    let [ range, char ] = passwordPolicy.split(" ");
    let [ min, max ] = range.split("-");
    let increment = 0;
    for (let passwdChar of passwd) if (passwdChar == char) increment++;
    if (min <= increment && increment <= max) result++;
  }
  return result;
}

function part2(arr) {
  let result = 0;// how many valid passwords there are
  for (let [ passwordPolicy, passwd ] of arr.map((s) => s.split(":"))) {
    let [ range, char ] = passwordPolicy.split(" ");
    let [ min, max ] = range.split("-");
    if (passwd.charAt(min) == char && passwd.charAt(max) != char || passwd.charAt(min) != char && passwd.charAt(max) == char) result++;
  }
  return result;
}

const arr = getInput().split("\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();