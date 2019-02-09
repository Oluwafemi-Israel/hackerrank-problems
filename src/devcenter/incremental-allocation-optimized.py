import math


# https://gist.github.com/mykeels/159b1bbe852104ed0a7a4c6a9b1e4f93


def incremental_allocation(n, m, x):
    # simplifying y(y+1)/2 - (x-1)(x-1+1)/2 < m
    # y^2 + y - [2m + (x-1)(x-1+1)] < 0
    # a is the coefficient of y^2
    # b is the coefficient of y
    # c is the constant

    one_to_x_minus_one = ((x - 1) * x) / 2
    a, b, c = 1, 1, -1 * 2 * (m + one_to_x_minus_one)

    y = ((-1 * b) + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    y = math.ceil(y)

    num_of_iterations = y - (x - 1)
    last_taker = num_of_iterations % n

    if last_taker == 0:
        return n - 1
    return last_taker - 1


assert (incremental_allocation(3, 11, 2) == 0)
assert (incremental_allocation(2, 11, 2) == 1)
assert (incremental_allocation(4, 11, 2) == 3)
assert (incremental_allocation(4, 44, 2) == 3)
assert (incremental_allocation(4, 44, 3) == 3)
assert (incremental_allocation(4, 44, 4) == 2)
assert (incremental_allocation(5, 101, 0) == 4)
assert (incremental_allocation(5, 70, 1) == 1)
