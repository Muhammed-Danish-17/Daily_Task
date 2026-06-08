/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    let lef = 0;
    let rig = 0;
    let mid = 0;

    for (let i of moves) {
        if (i === "L") {
            lef++;
        } else if (i === "R") {
            rig++;
        } else {
            mid++;
        }
    }

    return Math.abs(lef - rig) + mid;
};