# Sort the integers in ascending order by the number of 1's in their binary
# representations. For example, 7-> 111 and 8 -> 1000, so 8 (which has single 1
# in binary) would be ordered before 7 (which has triple 1's in binary). Two or
# more integers having the same number of 1's in their binary representations
# are ordered by increasing decimal value. For example, 5 -> 101 and 6-> 110 both
# contain double 1's in their binary representation, so 5 would be ordered
# before 6 because it has the smaller decimal value.


def sort_basis(elem):
    bit_count = "{0:b}".format(elem).count('1')
    # las las, we'll have strings of 2 characters
    # the first is the character mapped to the bit_count if the bit_count were an ascii code
    # the second is the character mapped to the decimal if the decimal were an ascii code
    # this way, we have the bit count taking precedence in sorting, and elements with the same bit count would be sorted
    # in ascending order of their decimal equivalents
    result = "{0}{1}".format(chr(bit_count), chr(elem))
    return result


def rearrange(elements):
    return sorted(elements, key=sort_basis)


if __name__ == '__main__':
    print(rearrange([5, 3, 7, 10, 14]))  # answer [3, 5, 10, 7, 14]
    print(rearrange([1, 2, 3]))
