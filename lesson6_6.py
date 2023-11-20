# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

result = []
numbers = [4, 3, 4, 5, 6, 7, 8, 8, 8, 9, 0, 1]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
for i in even_numbers:
    result.append(i)
for i in odd_numbers:
    result.append(i)

print(*result)
