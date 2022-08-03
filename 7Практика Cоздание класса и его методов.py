"""
Практика "Создание класса и его методов"
  (Класс точки)

  Рассмотрим точку в двумерном пространстве

"""
from math import sqrt

class Point:

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

""" При вызове класса Point эти аргументы становятся обязательными 
    Но если сделать x и y по умолчанию
"""
class Point:

    def __init__(self, coord_x=0, coord_y=0):# Теперь если мы не передадим коорднаты, то точка будет находися в начале координат
        self.x = coord_x
        self.y = coord_y

    def move_to(self, new_x, new_y):# Добавим поведение нашим точкам, переместим точку
        self.x = new_x
        self.y = new_y

    def go_home(self): # Перемещаем в начало координат
        self.x = 0
        self.y = 0

""" p3 = Point()
p3.move_to(4,5) -> атрибуты изменятся
"""

""" Заметим, что код у всех трех методов почти одинаковый,исправим это:
 
"""


class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):# Используем предыдущую функцию
        self.move_to(0,0)# Метод можем вызвать только от объекта через self

    def print_point(self): # Вывод координат точки
        print(f"Точка с координатами ({self.x}, {self.y}) ")

    def calc_dictance(self, another_point):# Метод для подсчета дистанции
        if not isinstance(another_point, Point):# Проверяем принадлежность классу Point
             raise ValueError("Аргумент должен принадлежать классу Точка") # Возбуждаем исключениe

        return sqrt((self.x - another_point.x)**2+(self.y - another_point.y)**2)

""" Такой принцип написания кода называется DRY - Донт репит юселф"""


class Point:
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self) # через класс обратимся к переменной, теперь в эту переменнюу будет добавляться новые точки как объект, к артибутам которого можно обратиться

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):# Используем предыдущую функцию
        self.move_to(0,0)# Метод можем вызвать только от объекта через self

    def print_point(self): # Вывод координат точки
        print(f"Точка с координатами ({self.x}, {self.y}) ")

    def calc_dictance(self, another_point):# Метод для подсчета дистанции
        if not isinstance(another_point, Point):# Проверяем принадлежность классу Point
             raise ValueError("Аргумент должен принадлежать классу Точка") # Возбуждаем исключениe

        return sqrt((self.x - another_point.x)**2+(self.y - another_point.y)**2)
