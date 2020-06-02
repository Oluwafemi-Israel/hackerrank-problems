def valid_longest_substring(s):
    start, end = 0, 0
    a_count, b_count = 0, 0

    for index, char in enumerate(s):
        if char == "a":
            b_count = 0
            a_count += 1

            if a_count > 2 and (index - end) > (end - start):
                start, end = end, index

        else:
            a_count = 0
            b_count += 1

            if b_count > 2 and (index - end) > (end - start):
                start, end = end, index

    if start == 0 and end == 0:
        return s
    return s[start:end]


if __name__ == "__main__":
    print(valid_longest_substring("aaa"))
    print(valid_longest_substring("aabbaaaaabb"))
    print(valid_longest_substring("aabbaabbaabbaa"))
    print(valid_longest_substring("baaabbabbb"))
    print(valid_longest_substring("babba"))
    print(valid_longest_substring("abaaaa"))
