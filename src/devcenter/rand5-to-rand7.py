import random


def rand5():
    return random.randint(1, 5)


def generate_bit():
    num = rand5()
    while num == 5:
        num = rand5()
    return num & 1


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
