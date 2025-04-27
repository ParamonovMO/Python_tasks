def sum_digits(number):
    num = list(str(number))
    return sum(map(int, num))


print(sum_digits(1234))
