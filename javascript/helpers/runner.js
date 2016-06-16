'use strict';

module.exports = function run(problem) {
    const startTime = new Date();
    const result = problem();
    const executionTime = new Date() - startTime;

    console.log(`execution time: ${executionTime}ms`);
    console.log(`result: ${result}`);
};