# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

list_of = ["hello", 5, "minsk", 6, 1, 3, 2, "567", 324]
# result = filter(lambda x: isinstance(x, str), list_of)
# print(*result)


def sorted_list(a):
    return isinstance(a, str)


new_list = filter(sorted_list, list_of)
print("строковый список: ", *new_list)
