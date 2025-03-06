/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    const N = grid.length * grid.length;
    const count = new Array(N + 1).fill(0);
    // for (let i = 0; i < grid.length; i++) {
    //     for (let j = 0; j < grid.length; j++) {
    //         count[grid[i][j]] += 1;
    //     }
    // }
    for (const row of grid) {
        for (const element of row) {
            count[element] += 1;
        }
    }
    let a = 0;
    let b = 0;
    for (let index = 1; index < N + 1; index++) {
        if (count[index] > 1) {
            a = index;
        } else if (count[index] == 0) {
            b = index;
        }

    }
    return [a, b];
};

console.log(findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])); // [6, 9]