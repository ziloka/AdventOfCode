function getInput(){
    // return `1-3 a: abcde
    // 1-3 b: cdefg
    // 2-9 c: ccccccccc`;
    return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr){
    let result = 0;// how many valid passwords there are
    for(let element of arr){
        let obj = element.split(":");
        let passwd = obj[1];
        let char = obj[0].split(" ")[1];
        let range = obj[0].split(" ")[0];
        let min = range.split("-")[0];
        let max = range.split("-")[1];
        let increment = 0;
        for(let passwdChar of passwd){
            if(passwdChar == char){
                increment++;
            }
        }
        if(min <= increment && max >= increment){
            result++;
        }
    }
    return result;
}

function part2(arr){
    let result = 0;// how many valid passwords there are
    for(let element of arr){
        let obj = element.split(":");
        let passwd = obj[1];
        let char = obj[0].split(" ")[1];
        let range = obj[0].split(" ")[0];
        let position1 = range.split("-")[0];
        let position2 = range.split("-")[1];
        if(passwd.charAt(position1) == char && passwd.charAt(position2) != char || passwd.charAt(position1) != char && passwd.charAt(position2) == char){
            result++;
        }
    }
    return result;
}

const input = getInput();
const arr = input.split("\n").map((s) => s.trim()); /// split, and trim space
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();