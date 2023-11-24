# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])



# list_of_numbers = [1, 2, 3, 4, 5, 6]
# new_items = []
#
# def reversed_list(list_of_numbers):
#     for number in range(len(list_of_numbers)):
#         new_items.append(list_of_numbers[len(list_of_numbers) - number - 1])
#
# reversed_list(list_of_numbers)
# print(new_items)

