# https://gist.github.com/mykeels/50efd7a127b771fb5c7a3a3dabe023fb


adjacent_keys = {
    '0': ['8'],
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8']
}


def phone_keypad_combinatorics(prev_combinations, n):
    if n == 1:
        return prev_combinations

    combinations = []
    for number in prev_combinations:
        for adjacent_key in adjacent_keys[number[-1]]:
            combinations.append("{}{}".format(number, adjacent_key))
    return phone_keypad_combinatorics(combinations, n - 1)


def f(d, n):
    return phone_keypad_combinatorics([str(d)], n)


if __name__ == '__main__':
    print("f(5, 1) = ", f(5, 1))
    print("f(1, 3) = ", f(1, 3))
    print("f(2, 3) = ", f(2, 3))
    print("f(3, 3) = ", f(3, 3))
    print("f(4, 3) = ", f(4, 3))
    print("f(5, 2) = ", f(5, 2))
    print("f(0, 4) = ", f(0, 4))
