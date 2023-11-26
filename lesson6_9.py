# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {
    1: {"name": "Nik", "surname": "Nikovich", "phone": "111111", "email": "Nik@gmail.com"},
    2: {"name": "Tom", "surname": "Tomovich", "phone": "222222"},
    3: {"name": "Sam", "surname": "Samovich", "phone": "333333", "email": "Sam@gmail.com"},
    4: {"name": "Dan", "surname": "Danovich", "phone": "444444", "email": ""}
}



def find_user(users: dict[int, dict[str, str, str, str]]):

    for user in users.values():
        if not user.get("email"):
            print(user)

find_user(users)




