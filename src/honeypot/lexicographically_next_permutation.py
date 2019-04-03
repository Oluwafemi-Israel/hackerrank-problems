def re_arrange_word(word):
    highest_index_i = 0
    highest_index_i_exists = False
    for i in range(len(word) - 1):
        if word[i] < word[i + 1]:
            highest_index_i = i
            highest_index_i_exists = True

    if not highest_index_i_exists:
        return 'no answer'

    highest_index_j = 0
    for j in range(highest_index_i + 1, len(word)):
        if word[j] > word[highest_index_i]:
            highest_index_j = j

    swapped_word = swap(word, highest_index_i, highest_index_j)
    return swapped_word[:highest_index_i + 1] + swapped_word[highest_index_i + 1:][::-1]


def swap(word, i, j):
    word = list(word)
    word[i], word[j] = word[j], word[i]
    return ''.join(word)


if __name__ == '__main__':
    print(re_arrange_word('xy'))
