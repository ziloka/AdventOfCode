const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

const validator = {
  "byr": (str) => 1920 <= str && str <= 2002,
  "iyr": (str) => 2010 <= str && str <= 2020,
  "eyr": (str) => 2020 <= str && str <= 2030,
  "hgt": (str) => {
    let valid = str.match(/^\d+(cm|in)$/) ?? false;
    let num = +str.slice(0, -2);
    if (!valid) return false; // return false if field contains invalid information
    return valid[1] == "in" ? 59 <= num && num <= 76 : 150 <= num && num <= 193
  },
  "hcl": (str) => /^#[0-9a-f]{6}$/.test(str),
  "ecl": (str) => /^(amb|blu|brn|gry|grn|hzl|oth)$/.test(str),
  "pid": (str) => /^[0-9]{9}$/.test(str)
};

function part1(passports) {
  return passports
    .filter((passport) => 
      Object.keys(validator)
        .every((key) => passport[key] != undefined)
    ).length;
}

function part2(passports) {
  return passports
    .filter((passport) => 
      Object.keys(validator)
        .every((key) => passport[key] != undefined && validator[key](passport[key]))
    ).length;
}

const passports = getInput().split("\n\n").map((s) => {
  let obj = {};
  for (let [key, value] of s.split(/\s|\n/).map((e) => e.split(":"))) {
    obj[key] = value;
  }
  return obj;
}); /// split, and trim space, convert string to struct
console.time();

console.log(`Number of passports: ${passports.length}`);
console.log(`part 1: ${part1(passports)}`);
console.log(`part 2: ${part2(passports)}`);
console.timeEnd();