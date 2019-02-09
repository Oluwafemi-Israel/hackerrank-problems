# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


def left_array_rotation(a, d):
    result = [0] * len(a)
    for i in range(len(a)):
        result[i - d] = a[i]
    return result
