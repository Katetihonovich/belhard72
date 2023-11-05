# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

# variant 1
sentence = input("enter text: ")
x = sentence.replace(" ", "-")
print(x)

# variant 2
statement = sentence.split(" ")
replaced_statement = "-".join(statement)
print(replaced_statement)
