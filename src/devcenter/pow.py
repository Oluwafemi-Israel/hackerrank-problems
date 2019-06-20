# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns
#  x^y.
#
# Do this faster than the naive method of repeated multiplication.

# Extremely good resource to help solve this
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation


def binary(num):
    result = ""
    quotient = num
    while quotient != 0:
        remainder = quotient % 2
        quotient = quotient // 2
        result = "{0}{1}".format(remainder, result)

    return result


def reduce_exponent(exponent):
    exponent_in_binary = binary(exponent)
    num_of_digits = len(exponent_in_binary)

    reduced_exponent = []

    for i in range(num_of_digits):
        if exponent_in_binary[num_of_digits - i - 1] == "1":
            reduced_exponent.append(2 ** i)

    return reduced_exponent


def generate_powers_of_2(base, greatest_exponent):
    memory = {1: base}
    current_exponent = 2
    while current_exponent <= greatest_exponent:
        memory[current_exponent] = memory[current_exponent // 2] ** 2
        current_exponent = current_exponent * 2

    return memory


def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    reduced_exponent = reduce_exponent(exponent)

    memory = generate_powers_of_2(base, reduced_exponent[-1])

    result = 1
    for exponent in reduced_exponent:
        result = result * memory[exponent]

    return result


if __name__ == "__main__":
    print(power(23, 123456))
