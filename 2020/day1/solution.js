function getInput(){
    return require('fs').readFileSync('./input.txt', 'utf8');
}

function part1(arr){
    let num1 = 0;
    let num2 = 0;
    for(let e1 of arr){
        for(let e2 of arr){
            if(e1+e2 == 2020){
                num1 = e1;
                num2 = e2;
                break;
            }
        }
    }
    return num1*num2;
}

function part2(arr){
    let num1 = 0;
    let num2 = 0;
    let num3 = 0;
    for(let e1 of arr){
        for(let e2 of arr){
            for(let e3 of arr){
                if(e1+e2+e3 == 2020){
                    num1 = e1;
                    num2 = e2;
                    num3 = e3;
                    break;
                }
            }
        }
    }
    return num1*num2*num3;
}

const input = getInput();
const arr = input.split("\n").map((s) => +s.trim()); /// split, and convert strings into numbers
console.time();

console.log(`part 1: ${part1(arr)}`);
console.log(`part 2: ${part2(arr)}`);
console.timeEnd();