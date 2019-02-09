# https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem
# TODO


def longest_increasing_sub_sequence(arr):
    lis = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return lis


if __name__ == '__main__':
    # arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    arr = [3, 4, -1, 0, 6, 2, 3]
    print(longest_increasing_sub_sequence(arr))
