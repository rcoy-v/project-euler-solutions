def square(x):
    return x**2

range_of_numbers = range(1, 101)
sum_of_squares = sum(map(square, range_of_numbers))
square_of_sum = square(sum(range_of_numbers))

print(square_of_sum - sum_of_squares)
