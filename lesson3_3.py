# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

# # variant_1
print("Hello new user, let's get to know each other!")
name = input("enter your name: ").strip()
age = input("enter your age: ").strip()
city = input("enter your city: ").strip()
print('Hello {} from {} who is {}!'.format(name, city, age))
print(f"Hello {name} from {city} who is {age}!".format(name=name, age=age, city=city))

# # variant 2
print("Hello %(name)s from %(city)s who is %(age)s!" % {"name": name, "city": city, "age": int(age)})
print("Hello %s from %s who is %s!" % (name, city, int(age)))

# variant 3
print(f"Hello {name} from {city} who is {age}!")

# # variant 4
print("Hello new user, let's get to know each other!")
user = input("Enter your Name, age, City: ").strip()
words = user.split(", ")
user_name = words[0]
user_age = words[1]
user_city = words[2]
print(f"Hello {user_name} from {user_city} who is {user_age}!")

# # variant 5
print("Hello new user, let's get to know each other!")
name = input("enter your name: ")
while not name.isalpha():
    name = input("you didn't enter your name, please enter your name: ")
age = input("enter your age: ")
while not age.isdigit():
    age = (input("you didn't enter your age, please enter age: "))
city = input("enter your city: ")
while not city.isalpha():
    city = (input("you didn't enter your city, please enter the city: "))
print('Hello {} from {} who is {}!'.format(name, city, age))

