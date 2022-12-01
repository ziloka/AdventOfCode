const getInput = () => require('fs').readFileSync('./input.txt', 'utf8');

const validator = {
  "byr": (value) => 1920 <= value && value <= 2002,
  "iyr": (value) => 2010 <= value && value <= 2020,
  "eyr": (value) => 2020 <= value && value <= 2030,
  "hgt": (value) => {
    let valid = value.match(/^\d+(cm|in)$/) ?? false;
    let num = +value.slice(0, -2);
    if (!valid) return false; // return false if field contains invalid information
    return valid[1] == "in" ? 59 <= num && num <= 76 : 150 <= num && num <= 193
  },
  "hcl": (value) => /^#[0-9a-f]{6}$/.test(value),
  "ecl": (value) => /^(amb|blu|brn|gry|grn|hzl|oth)$/.test(value),
  "pid": (value) => /^[0-9]{9}$/.test(value)
};

const passports = getInput().split("\n\n").map((s) => {
  let obj = {};
  for (let [key, value] of s.split(/\s|\n/).map((e) => e.split(":"))) {
    obj[key] = value;
  }
  return obj;
}); // split, and trim space, convert string to struct

const validate = (func) => passports
  .filter((passport) =>
    Object.keys(validator)
      .every((key) => passport[key] != undefined && func(passport, key))
  ).length;

console.time();

console.log(`part 1: ${validate(() => true)}`);
console.log(`part 2: ${validate((passport, key) => validator[key](passport[key]))}`);
console.timeEnd();