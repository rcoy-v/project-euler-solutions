from time import time

start_time = time()


def is_palindrome(number):
    return str(number) == str(number)[::-1]


largest_palindrome = 0
a = 999
while a >= 100:
    if a % 11 == 0:
        b = 999
        step_b = 1
    else:
        b = 990
        step_b = 11
    while b >= a:
        if a * b <= largest_palindrome:
            break
        if is_palindrome(a * b):
            largest_palindrome = a * b
        b -= step_b
    a -= 1
print(largest_palindrome)
print(time() - start_time)