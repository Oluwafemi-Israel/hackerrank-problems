# https://www.hackerrank.com/challenges/30-conditional-statements/submissions/code/90188322


if __name__ == '__main__':
    N = int(input())

    if N % 2 == 0:
        if 2 <= N <= 5:
            print('Not Weird')
        elif 6 <= N <= 20:
            print('Weird')
        elif N > 20:
            print('Not Weird')
    else:
        print('Weird')

