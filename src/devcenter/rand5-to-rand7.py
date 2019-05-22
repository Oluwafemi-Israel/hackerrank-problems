import random


def rand5():
    return random.randint(1, 5)


def generate_bit():
    num = rand5()
    while num == 5:
        num = rand5()
    return num & 1


# This may not be the most efficient, but it works
#
# 7 can be represented by 3 bits.
#
# If we employ rand5() in generating 1s or 0s with equal probability, we can populate the 3 required bits.
#
# The question of how to generate 1s or 0s remains. One idea is to use the oddness or evenness of rand5()
# to select the bit `e.g odd gives 1, even gives 0`.
# However, there are 3 possible odds, and 2 possible evens for rand5().
# To level the playing ground we pick any of the odds and reject it always (e.g 5)
def rand7():
    sum_ = 0
    while sum_ == 0:
        for k in range(1, 4):
            sum_ = (sum_ << 1) + generate_bit()
    return sum_


if __name__ == "__main__":
    frequencies = [0] * 7
    number_of_tries = 1000000

    for i in range(number_of_tries):
        frequencies[rand7() - 1] += 1

    print(frequencies)

    for index, frequency in enumerate(frequencies):
        print("{0} ~ {1}%".format(index + 1, frequency / number_of_tries))
