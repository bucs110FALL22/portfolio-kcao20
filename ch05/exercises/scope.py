def multiply(a, b):
    sum = 0
    for i in range(b):
        sum += a
    return sum


def exponent(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result


def square(a):
    return exponent(a, 2)


if __name__ == "__main__":
    print(multiply(5, 8))
    print(exponent(3, 4))
    print(square(15))
