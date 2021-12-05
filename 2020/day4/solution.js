function getInput(){
  return require('fs').readFileSync('./input.txt', 'utf8');
}

function convertPassport(passportStr){
  let obj = {}
  for(let item of passportStr.split(/\s|\n/)){
    let items = item.split(":");
    let key = items[0];
    let value = items[1];
    obj[key] = value;
  }
  return obj;
}

function part1(arr){
  let result = 0;
  for(let passportStr of arr){
    let passport = convertPassport(passportStr);
    if(
      passport.byr != undefined && 
      passport.ecl != undefined &&
      passport.eyr != undefined &&
      passport.hcl != undefined &&
      passport.hgt != undefined && 
      passport.iyr != undefined &&
      passport.pid != undefined
    ){
      result++;
    }
  }
  return result;
}

function part2(arr){
  let result = [];
  let writeStr = "";
  let validator = {
    "byr": (str) => 1920 <= str && str <= 2002,
    "iyr": (str) => 2010 <= str && str <= 2020,
    "eyr": (str) => 2020 <= str && str <= 2030,
    "hgt": (str) => {
      let regex = /^\d+(cm|in)$/;
      let valid = str.match(regex) ?? false;
      let num = str.slice(0, -2)
      if(!valid) return false;
      return valid[1] == "in" ? 59 <= num && num <= 76 : 150 < num && num <= 193
    },
    "hcl": (str) => /^#[0-9a-f]{6}$/.test(str),
    "ecl": (str) => /^(amb|blu|brn|gry|grn|hzl|oth)$/.test(str),
    "pid": (str) => /^[0-9]{9}$/.test(str)
  }
  let validatorKeys = Object.keys(validator);
  for(let i=0;i<arr.length;i++){
    let passportStr = arr[i].replace(/\n/g, " ");
    let passport = convertPassport(passportStr);
    let flag = true;
    let keys = Object.keys(passport);
    if(keys.filter((k) => validatorKeys.includes(k)) == validatorKeys.length) continue;
    // if(!validatorKeys.every((s) => keys.includes(s))) continue; // make sure all required keys are there, have not checked value yet
    for(let key of keys){
      if(key == "cid") continue; // ignore cid property, it is optional
      let value = passport[key];
      if(validator[key] == undefined || validator[key](value) == false){
        flag = false;
        break;
      }
    }
    if(flag == true){
      result.push(passport);
    }
  }

  return result.length;
}

const input = getInput();
const arr = input.split("\n\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`Number of passports: ${arr.length}`);
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();