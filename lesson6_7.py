# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

list_of_numbers = [1, 2, 3, 4, 5]



n = len(list_of_numbers)-1
for i in range(n):
    print(list_of_numbers[i-1]+list_of_numbers[i+1], end=' ')




