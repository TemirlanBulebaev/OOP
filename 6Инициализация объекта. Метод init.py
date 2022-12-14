"""Инициализация объекта. Метод init"""

class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

""" 
Вызывать метод для создания атрибутов не совсем удобно, поэтому познакомимся с методом __init__

Магический метод в питоне:
    1)У таких методов название начинается с двух нижних подчеркиваний и заканчивается ими
    2) Особенность таких методов:
        Каждый из этих методов автоматически будет срабатывать в определенный момент, 
        наш метод __init__ будет срабатывать ровно после создания объкта 
            tom = Cat() -> <__main__.Cat at 0x177dd3b69d0> и выведется Hello
"""

class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self):
        print('Hello')

"""
        def __init__(self):
        print('Hello')
        
    Этот метод принимает экземпляр (через self), который создается в процессе вызова нашегот класса- внтурь этого метода
    Метод __init__  принимает на вход наш объект, который мы вновь создаем
    Он нужен для инициализации, для заполнения объекта какими-лио значениями 
    
    Мы можем заполнить объект в момент инициализации и делается это так:
        def __init__(self, name, breed, age, color): Перечисляем параметры , которые хотим увидеть
        print('Hello')
        
>>> Cat('Tom', 'siam', 40, 'black') ->  Мы их увидим при выводе, а значит внутри функции __init__ 
                                        Мы сможем ими воспользоваться 
    Теперь избавляемся от метода set_value

"""
class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

"""
>>> walt = Cat('Walt')

    Теперь наш экземпляр имеет свои атрибуты, которые мы проставили в момент инициализации
    
"""