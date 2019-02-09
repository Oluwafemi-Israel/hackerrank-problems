# https://www.hackerrank.com/challenges/reduced-string/problem


# Complete the superReducedString function below.
def super_reduced_string(input_string):
    i = 0
    while i < len(input_string) - 1:
        if input_string[i] == input_string[i + 1]:
            input_string = input_string[:i] + input_string[i + 2:]
            i = 0
        else:
            i += 1

    if input_string:
        return input_string
    return 'Empty String'
