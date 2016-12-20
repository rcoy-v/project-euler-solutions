from time import time

start_time = time()
largest_palindrome = 0


def is_palindrome(number):
    return str(number) == str(number)[::-1]


for x in reversed(range(100, 1000)):
    for y in reversed(range(100, 1000)):
        product = x * y
        if is_palindrome(product):
            largest_palindrome = max(largest_palindrome, product)

print(largest_palindrome)
print(time() - start_time)

