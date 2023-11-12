# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

from collections import *

text = input("Enter any text: ")
numb_ent = {i: text.count(i) for i in text if i.isalpha()}
print(numb_ent)



# letters_count = Counter(text)
# print(letters_count)