# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры


n = int(input("enter any number :"))
data = {i: {"name": input("enter your name:"), "email": input("enter your email:")} for i in range(0, n+1)}
print(data)

