def splitInteger(num, parts):
    # your code here
    quotient = num // parts
    remainder = num % parts
    result = [quotient] * parts

    if remainder == 0:
        return result
    else:
        i = 0
        while remainder != 0:
            result[i] += 1
            remainder -= 1
            i += 1
        return result


if __name__ == "__main__":
    print(splitInteger(20, 6))
