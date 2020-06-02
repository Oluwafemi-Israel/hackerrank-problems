def is_palindrome_permutation(s):
    s = s.lower()
    bit_vector = 0 << 25

    for char in s:
        index = ord(char) - 97
        bit_vector = (1 << index) ^ bit_vector

    return (bit_vector - 1) & bit_vector == 0


def min_adjacent_swaps(s):
    if is_palindrome_permutation(s):
        s = list(s)
        i, j = 0, len(s) - 1
        total_swaps = 0

        while j > i:
            k = j
            while k > i and s[i] != s[k]:
                k -= 1

            # When a matching pair is found at position k, push this character forward until position j
            # We do this so the characters at position i and j to match
            while k < j:
                if s[i] == s[j]:
                    # this is only possible when the character at i is that single character with no matching pair
                    # in this case: i==k. Pushing the character at k is also pushing the character at i
                    # so it is possible that the character at i becomes equal to the character at j
                    # this is out intended goal. Once this goal is achieved, break from the loop.
                    break
                s[k], s[k + 1] = s[k + 1], s[k]
                total_swaps += 1
                k += 1

            i += 1
            j -= 1

        return total_swaps
    else:
        return -1

# #####################################################################
# ALTERNATIVE APPROACH
# This may be easier to understand that the previous approach
# #####################################################################
# def min_number_of_adjacent_swaps(s):
#     if is_permutation_of_palindrome(s):
#         s = list(s)
#         i, j = 0, len(s) - 1
#         total_swaps = 0
#
#         while j > i:
#             if s[i] != s[j]:
#                 k = j
#                 while k > i and s[i] != s[k]:
#                     k -= 1
#
#                 if i == k:
#                     # This character is the only character with no matching pair, hence it must be in the middle
#                     # the goal is to push it forward one step at a time
#                     s[i], s[i + 1] = s[i + 1], s[i]
#                     total_swaps += 1
#                 else:
#                     # When a matching pair is found at position k, push this character forward until position j
#                     while k < j:
#                         s[k], s[k + 1] = s[k + 1], s[k]
#                         total_swaps += 1
#                         k += 1
#                     i += 1
#                     j -= 1
#             else:
#                 i += 1
#                 j -= 1
#
#         return total_swaps
#     else:
#         return -1


if __name__ == "__main__":
    assert min_adjacent_swaps("mamad") == 3
    assert min_adjacent_swaps("asflkj") == -1
    assert min_adjacent_swaps("aabb") == 2
    assert min_adjacent_swaps("ntiiiin") == 2
    assert min_adjacent_swaps("mallam") == 0

