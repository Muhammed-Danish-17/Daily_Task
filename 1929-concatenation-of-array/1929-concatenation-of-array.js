/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let dup = [];

    for (let i of nums) {
        dup.push(i);
    }

    for (let i of nums) {
        dup.push(i);
    }

    return dup;
};