"""
https://leetcode.com/discuss/interview-question/398026/
"""


def solution(string):
    i, j = 0, 1
    moves = 0

    while j < len(string):
        if string[j] != string[i]:
            moves += (j - i) // 3
            i = j
        j += 1

    moves += (j - i) // 3

    return moves


if __name__ == "__main__":
    assert solution("baaaaaa") == 2
    assert solution("") == 0
    assert solution("a") == 0
    assert solution("baaaaa") == 1
    assert solution("baaabbaabbba") == 2
    assert solution("baabab") == 0
