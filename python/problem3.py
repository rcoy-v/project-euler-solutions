#!/usr/bin/env python3
import math


def prime_factors(number):
    max_factor = math.sqrt(number)
    prime_factors = []

    if number % 2 == 0:
        number /= 2
        prime_factors.append(2)
        while number % 2 == 0:
            number /= 2
    factor = 3
    while number > 1 and factor <= max_factor:
        if number % factor == 0:
            number /= factor
            prime_factors.append(factor)
            while number % factor == 0:
                number /= factor
        factor += 2
    return prime_factors

print(prime_factors(600851475143))


