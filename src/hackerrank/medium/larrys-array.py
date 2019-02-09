# https://www.hackerrank.com/challenges/larrys-array/problem


def merge_sort_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]

        a, ai = merge_sort_inversions(a)
        b, bi = merge_sort_inversions(b)
        c = []

        i = 0
        j = 0
        inversions = 0 + ai + bi

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)

    c += a[i:]
    c += b[j:]

    return c, inversions


def is_solvable(grid_width, inversions, blank):
    if (grid_width % 2 != 0 and inversions % 2 == 0) or (
            grid_width % 2 == 0 and ((blank % 2 != 0) == (inversions % 2 == 0))):
        return 'YES'
    return 'NO'


# Complete the larrys_array function below.
def larrys_array(arr):
    n = len(arr)
    grid_width = 3

    if n % grid_width != 0:
        for i in range(grid_width - (n % grid_width)):
            arr.append(n + i)

    sorted_arr, num_of_inversions = merge_sort_inversions(arr)
    return is_solvable(grid_width, num_of_inversions, 0)
