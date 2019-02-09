# https://gist.github.com/mykeels/159b1bbe852104ed0a7a4c6a9b1e4f93


def incremental_allocation(n, m, x):
    i, running_sum = -1, 0
    while running_sum < m:
        i += 1
        running_sum += (x + i)
    return i % n


assert (incremental_allocation(3, 11, 2) == 0)
assert (incremental_allocation(2, 11, 2) == 1)
assert (incremental_allocation(4, 11, 2) == 3)
assert (incremental_allocation(4, 44, 2) == 3)
assert (incremental_allocation(4, 44, 3) == 3)
assert (incremental_allocation(4, 44, 4) == 2)
assert (incremental_allocation(5, 101, 0) == 4)
assert (incremental_allocation(5, 70, 1) == 1)
