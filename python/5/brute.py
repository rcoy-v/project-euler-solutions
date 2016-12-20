import functools


def greatest_common_divisor(a, b):
    return greatest_common_divisor(b, a % b) if b > 0 else a


def least_common_multiple(a, b):
    return (a * b) / greatest_common_divisor(a, b)


print(int(functools.reduce(least_common_multiple, range(1, 21))))

