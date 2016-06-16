// Largest prime factor
'use strict';

const run = require('../helpers/runner');

function isPrime(number) {
    for (let i = 2; i <= number; i++) {
        if (number % i === 0) {
            if (i < number) {
                return false;
            }
            return true;
        }
    }
}

function findNextPrime(start) {
    let nextPrime = start;

    while (true) {
        if (isPrime(nextPrime)) {
            return nextPrime;
        }
        nextPrime += 1;
    }
}

run(() => {
    const primeFactorizationNumber = 600851475143;
    const primes = [2];
    const primeFactors = [];

    let currentFactorization = primeFactorizationNumber;

    while (currentFactorization > 1) {
        const primeFactor = primes.find((prime) => {
            return currentFactorization % prime === 0;
        });

        if (primeFactor) {
            primeFactors.push(primeFactor);
            currentFactorization /= primeFactor;
        } else {
            const nextPrimeSearchStart = primes[primes.length - 1] + 1;

            primes.push(findNextPrime(nextPrimeSearchStart));
        }
    }

    return primeFactors.reduce((maxPrime, nextPrime) => {
        return Math.max(maxPrime, nextPrime);
    });
});
