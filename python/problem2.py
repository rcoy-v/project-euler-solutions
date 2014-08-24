#!/usr/bin/env python3
def fibonacci(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a + b

print(sum(x for x in fibonacci(4000000) if x % 2 == 0))

