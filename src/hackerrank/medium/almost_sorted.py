# https://www.hackerrank.com/challenges/almost-sorted/problem
# TODO


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def first_and_last_unsorted(arr):
    for i in range(len(arr)):
        if arr[i] >= arr[i + 1]:
            break

    for j in range(len(arr) - 1, i, -1):
        if arr[j] < arr[j - 1]:
            break

    return i, j


# Complete the almostSorted function below.
def almost_sorted(arr):
    if not is_sorted(arr):
        start, end = first_and_last_unsorted(arr)

        arr[start], arr[end] = arr[end], arr[start]
        if is_sorted(arr):
            return 'yes\nswap {0} {1}'.format(start + 1, end + 1)
        else:
            arr[start + 1:end] = arr[start + 1:end:-1]
            if is_sorted(arr):
                return 'yes\nreverse {0} {1}'.format(start + 1, end + 1)
            return 'no'
    return 'yes'


if __name__ == '__main__':
    n = int(input())
    # while True:
    arr = list(map(int, input().rstrip().split()))
    print(almost_sorted(arr))
