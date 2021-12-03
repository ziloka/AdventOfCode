function getInput(){
  // return `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
  //         byr:1937 iyr:2017 cid:147 hgt:183cm

  //         iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
  //         hcl:#cfa07d byr:1929

  //         hcl:#ae17e1 iyr:2013
  //         eyr:2024
  //         ecl:brn pid:760753108 byr:1931
  //         hgt:179cm

  //         hcl:#cfa07d eyr:2025 pid:166559648
  //         iyr:2011 ecl:brn hgt:59in`;
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
      passport.iyr != undefined
    ){
      result++;
    }
  }
  return result;
  // let result = 0;
  // // cid is optional
  // // let passportData = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'];
  // let passportData = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'];
  // for(let passport of arr){
  //   let properties = [];
  //   for(let prop of passport.split(" ").filter((s) => s.length != 0)) properties.push(prop.split(":")[0].trim());
  //   if(properties.every(p => passportData.includes(p))){
  //     result++;
  //   } else {
  //     console.log(passport);
  //     // console.log(properties.sort().filter((s) => s != "cid"));
  //   }
  // }
  // return result;
}

function part2(arr){
 
}

const input = getInput();
const arr = input.split("\n\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`Number of passports: ${arr.length}`);
console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();