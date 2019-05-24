def bit_wise_sum(x, y):
    sum_ = x ^ y
    carry = x & y

    while carry != 0:
        carry = carry << 1
        x = sum_
        y = carry
        sum_ = x ^ y
        carry = x & y

    return sum_


if __name__ == "__main__":
    print(bit_wise_sum(3, 1))
