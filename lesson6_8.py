# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

world = {
    "Belarus": ["Brest", "Minsk", "Gomel", "Mogilev"],
    "Poland": ["Warsaw", "Gdansk", "Krakow", "Lodz"],
    "RSA": ["Johannesburg", "Pretoria", "CapeTown"]
}
city = input()


def find_country():
    for country, cities in world.items():
        if city in cities:
            print(f'INFO: {city} is in {country}')
            break
    else:
        print(f'ERROR: Country for {city} not found')


find_country()
