# Вывести первые N чисел кратные M и больше K

m = int(input())
k = int(input())
n = int(input())
counter = 0
for i in range(0, 100):
    if i % m == 0 and i > k:
        print(i)
        counter = counter+1
    if counter == n:
        break
#
#
# for i in range(1, 100):
#     if i % m == 0 and i > k:
#         print(i)
#         n -= 1
#     if n == 0:
#         break

# i = 1
# while True:
#     if i % m == 0 and i > k:
#         print(i)
#         n -= 1
#     if n == 0:
#         break
#     i = i+1
