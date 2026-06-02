var judgeCircle = function(moves) {
    let x = 0;
    let y = 0;

    for (let m of moves) {
        if (m === "U") {
            x += 1;
        } else if (m === "D") {
            x -= 1;
        } else if (m === "R") {
            y += 1;
        } else {
            y -= 1;
        }
    }

    return x === 0 && y === 0;
};