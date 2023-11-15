# Вывести четные числа от 2 до N по 5 в строку

# d = []
n = int(input())
# for i in range(2, n+1):
#      if i % 2 == 0:
#          d.append(i)
# for i in range(0, len(d)):
#     print(str(d[i])+' ', end="")
#     if i % 5 == 4:
#          print("\n")


numbers = []
for i in range(2, n+1):
    if i % 2:
        continue
    numbers.append(i)
for i in range(0, len(numbers), 5):
    print(*numbers[i:i + 5])
