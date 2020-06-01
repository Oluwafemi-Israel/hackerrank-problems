"""
https://leetcode.com/discuss/interview-question/365872/
"""


def compute_digit_sum(num):
    digit_sum = 0

    while num > 0:
        digit_sum += (num % 10)
        num = num // 10

    return digit_sum


def solution(arr):
    store = {}
    result = -1

    for num in arr:
        digit_sum = compute_digit_sum(num)

        if digit_sum not in store:
            store[digit_sum] = num
        else:
            result = max(result, num + store[digit_sum])
            store[digit_sum] = max(num, store[digit_sum])

    return result


if __name__ == "__main__":
    assert solution([51, 71, 17, 42]) == 93
    assert solution([42, 33, 60]) == 102
    assert solution([51, 32, 43]) == -1
