# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

list_of = ["hello", 5, "minsk", 6, 1, 3, 2, "567", 324]
result = filter(lambda x: type(x) is str, list_of)
print(*result)


