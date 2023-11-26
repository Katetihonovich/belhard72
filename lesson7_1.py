# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:
    def __init__(self, color, seats, babyseat):
        self.color = color
        self.count_passengers_seats = int(seats)
        self.is_baby_seat = babyseat
        self.is_busy = False

    def __str__(self):
        return f"Цвет - {self.color}, количество мест - {self.count_passengers_seats}, детское кресло - {self.is_baby_seat}, свободно - {self.is_busy}"

car = Car(color="red", seats=7, babyseat=True)

print(str(car))
