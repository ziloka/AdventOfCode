let slopeResult = 0;
let previousXValue = 0; // starting x point
for (let i = slope.d; i < arr.length; i += slope.d) { // on each iteration the y position gets shifted by 1
  let str = arr[i];
  previousXValue += slope.r; // the x position to check
  if (previousXValue >= str.length) { // check if we are unable to access character at specified position
    // generate longer string so we can access the char position
    let temp = "";
    for (let i = 0; i <= Math.ceil(previousXValue / str.length); i++) { // identify least amount of iterations in order to access char position
      temp += str;
    }
    str = temp;
  }
  // access string
  if (str.charAt(previousXValue) == "#") { // if at specific position was a tree, # is a tree
    slopeResult++;
  }
}