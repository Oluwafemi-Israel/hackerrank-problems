# https://www.hackerrank.com/challenges/pangrams/problem


# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    for letter in range(97, 123):
        print(chr(letter))
        if chr(letter) not in s:
            return 'not pangram'
    return 'pangram'
