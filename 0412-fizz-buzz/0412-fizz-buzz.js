/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let strr = [];
    
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            strr.push("FizzBuzz");
        } else if (i % 3 === 0) {
            strr.push("Fizz");
        } else if (i % 5 === 0) {
            strr.push("Buzz");
        } else {
            strr.push(i.toString());
        }
    }
    
    return strr;
};