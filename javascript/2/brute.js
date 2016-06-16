// Even Fibonacci numbers
'use strict';

const run = require('../helpers/runner');

run(() => {
    const ceiling = 4000000;

    const currentFibonacci = [1, 2];
    let evenFibonacciSum = 0;

    while (currentFibonacci[1] < ceiling) {
        if (currentFibonacci[1] % 2 === 0) {
            evenFibonacciSum += currentFibonacci[1];
        }

        const nextFibonacci = currentFibonacci[0] + currentFibonacci[1];

        currentFibonacci[0] = currentFibonacci[1];
        currentFibonacci[1] = nextFibonacci;
    }

    return evenFibonacciSum;
});