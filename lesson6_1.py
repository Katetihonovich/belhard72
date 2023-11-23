# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


a = 111


def binary(a):
    return bin(a)


print(binary(a))


def decimal(a):
    return eval(binary(a))


print(decimal(a))
