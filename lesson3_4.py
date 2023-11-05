# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

input_string = input("Please enter any numbers: ")
numbers_list = input_string.split("," or " ")
pos = [num for num in numbers_list if float(num) > 0]
pos_count = len(pos)
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", len(numbers_list) - pos_count)
