'''Объект - контейнер, состоящий из:
    1) Данных и состояния - атрибуты
    2) Поведения - методы объекта

  Каждый объект в питоне принадлежит определенному классу ( можно проверить через type() )

'''
type(4) # int
type('s')# str

""" У int есть множенство экземпляров класса, например: 1, 2, 3, 4
    у list экземпляры класса это [1,2], [2,3] и т.д. 
"""

""" Принадлежность объекта к какому-то  классу можно проверить через функции """
isinstance(4, int)# Передаем сначала объект, потом класс = True
isinstance(4, float) # = False
isinstance(4, object)#=True
isinstance(True, object) # True
isinstance(int, float) # Даже сами классы являются объектом

""" Но если проверять type(int) будет сам type"""

""" Класс - это шаблон при помощи которого мы будем создавать объекты
    Как создать класс:
"""
class Car: #Имя с большой буквы
    pass

a =  Car() # Вызывает класс, результатом вызова будет возвращение экземпляра класса
# Переменная a - объект класса Car type(a)->__main__.Car
isinstance(a, Car)# True

# Мы можем создавать множество объектов на основе класса Car
b = Car()

# Создадим класс с данными, которые будут присваиваться объектам при создании
class Car:
    model = 'BMW'
    engine = 1.6

c = Car()

d = Car()

#Теперь в этих переменных хранятся данные из класса Car()