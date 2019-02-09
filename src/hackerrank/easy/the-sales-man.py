# https://www.hackerrank.com/contests/world-codesprint-12/challenges/the-salesman/problem


def minimumTime(x):
    #  Return the minimum time needed to visit all the houses.
    return max(x) - min(x)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        x = list(map(int, input().strip().split(' ')))
        result = minimumTime(x)
        print(result)
