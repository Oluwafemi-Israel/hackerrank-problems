# This problem is a variation of this problem
# https://www.hackerrank.com/challenges/linkedin-practice-divisible-sum-pairs/problem
# Look for pairs of songs that add up to whole minutes
# Amazing explanation can be found here
# https://www.hackerrank.com/challenges/linkedin-practice-divisible-sum-pairs/forum/comments/195413


# Brute Force Approach
# def playlist(songs):
#     # Write your code here
#     songs_len = len(songs)
#     pairs = 0
#     for i in range(songs_len):
#         for j in range(i+1, songs_len):
#             if (songs[i] + songs[j]) % 60 == 0:
#                 pairs += 1
#     return pairs


def playlist(songs):
    sum_ = 3

    freq = [0] * sum_

    for song in songs:
        freq[song % sum_] += 1

    count = freq[0] * (freq[0] - 1) / 2

    if (sum_ % 2) == 0:
        count += freq[sum_ // 2] * (freq[sum_ // 2] - 1) / 2

    i = 1
    while i <= (sum_ // 2):
        count += freq[i] * freq[sum_ - i]
        i += 1

    return int(count)


if __name__ == "__main__":
    print(playlist([1, 3, 2, 6, 1, 2]))
