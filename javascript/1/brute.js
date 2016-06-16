// Multiples of 3 and 5
'use strict';

const run = require('../helpers/runner');

run(() => {
    const ceiling = 999;
    const multiplesOf3And5 = [];
    const rangeOfPossibleMultiples = Array.from({length: ceiling}, (v, k) => k + 1);

    rangeOfPossibleMultiples.forEach((possibleMultiple) => {
        if (possibleMultiple % 5 === 0 || possibleMultiple % 3 === 0) {
            multiplesOf3And5.push(possibleMultiple);
        }
    });

    return multiplesOf3And5.reduce((sum, next) => sum + next);
});
