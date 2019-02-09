# https://www.hackerrank.com/contests/apt-coding-challenge/challenges/save-the-prisoner

import os


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    m %= n
    resp = (m + s - 1) % n
    if resp == 0:
        resp = n
    return resp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
