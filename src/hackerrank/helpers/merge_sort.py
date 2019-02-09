def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr) / 2]
        b = arr[len(arr) / 2:]

        a = merge_sort(a)
        b = merge_sort(b)
        c = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1

        c += a[i:]
        c += b[j:]

    return c


if __name__ == '__main__':
    print(merge_sort([3, 5, 9, 21, 2, 1]))
