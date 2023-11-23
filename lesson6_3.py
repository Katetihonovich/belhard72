# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
step = int(input("enter number: "))


def shifts(list_of_numbers, step):
    if step < 0:
        step = abs(step)
        for i in range(step):
            list_of_numbers.append(list_of_numbers.pop(0))
    else:
        for i in range(step):
            list_of_numbers.insert(0, list_of_numbers.pop())

shifts(list_of_numbers, step)
print(list_of_numbers)