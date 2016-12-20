from math import floor, sqrt


def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0:
        return False
    if x < 9:
        return True
    if x % 3 == 0:
        return False

    root = floor(sqrt(x))
    form = 5
    while form <= root:
        if x % form == 0:
            return False
        if x % (form + 2) == 0:
            return False
        form += 6

    return True


current_number = 1
prime_count = 1

while prime_count < 10001:
    current_number += 2
    if is_prime(current_number):
        prime_count += 1

print(current_number)
