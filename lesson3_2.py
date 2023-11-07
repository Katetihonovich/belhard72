# # Пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
# # variant 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
sum_of_3 = num1 + num2 + num3
avg = sum_of_3 / 3
# print('%.3f ' % avg)
print(round(avg, 3))

# # variant 2
num = input("type 3 numbers: ")
num1 = num.split(" ")
print(round((float(num1[0]) + float(num1[1]) + float(num1[2]))/float(len(num1)), 3))
