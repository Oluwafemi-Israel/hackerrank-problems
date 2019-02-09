# https://www.hackerrank.com/contests/apt-coding-challenge/challenges/square-configurations

def num_of_squares(m, n):
    m, n = min(m, n), max(m, n)
    res = (m * (m + 1) * ((3 * n) - m + 1)) / 6
    return res


def solve(d):
    results = []
    results_inverse = []

    m = 1
    n = d
    while m <= n:
        n = ((6 * d) / ((3 * m) * (m + 1))) + (m / 3) - (1 / 3)
        if num_of_squares(m, n) == d and m <= n:
            if (m, n) not in results:
                results.append((m, n))
                if n != m and (n, m) not in results and (n, m) not in results_inverse:
                    results_inverse.append((n, m))

        n = ((6 * d) / ((3 * m) * (m + 1))) + (m / 3) - (1 / 3)+1
        if num_of_squares(m, n) == d and m <= n:
            if (m, n) not in results:
                results.append((m, n))
                if n != m and (n, m) not in results and (n, m) not in results_inverse:
                    results_inverse.append((n, m))
        m += 1
    return results + results_inverse[::-1]


if __name__ == '__main__':
    d = int(raw_input().strip())

    ans = solve(d)
    print(len(ans))
    for pair in ans:
        print pair[0], pair[1]
