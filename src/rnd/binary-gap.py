# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by
# ones at both ends in the binary representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function: function solution(N); that, given a positive integer N, returns the length of its longest binary
# gap. The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
# longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
# Write an efficient algorithm for the following assumptions: N is an integer within the range [1..2,147,483,647].


def binary_gap(n):
    i, j, k = 0, 0, 0
    seen_first_one, seen_first_zero = False, False
    max_gap = 0

    while n > 0:
        remainder = n % 2
        n = n // 2

        if remainder == 1 and not seen_first_one:
            seen_first_one = True

        if seen_first_one:
            if remainder == 0:
                if not seen_first_zero:
                    seen_first_zero = True
                    j, k = i, i
                else:
                    j += 1
            else:
                if seen_first_zero:
                    max_gap = max(max_gap, j - k + 1)
                    seen_first_zero = False

        i += 1

    return max_gap


assert (2 == binary_gap(9))
assert (4 == binary_gap(529))
assert (1 == binary_gap(20))
assert (0 == binary_gap(15))
assert (0 == binary_gap(32))
assert (5 == binary_gap(1041))
