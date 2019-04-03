def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def permutation(string, prefix):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[:i] + string[i+1:]
            permutation(rem, prefix+string[i])


if __name__ == '__main__':
    # print(reverse_array([1, 2, 3, 4, 5]))
    # print(reverse_array([1, 2, 3, 4]))
    permutation("man", "")
