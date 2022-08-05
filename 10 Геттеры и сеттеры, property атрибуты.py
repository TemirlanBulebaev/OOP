""" Геттеры и сеттеры, property атрибуты
"""


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

""" Атрибуты являются публичными мы можем к ним обратиться
 
Давайте ограничим доступ к переменной balance, но предостивим некий интерфейс,чтобы получить доступ к этой переменной


 """
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значения
        return self.__balance

    def set_balance(self, value):# Поставит значение
        if not isinstance(value, (int, float)): # Проверка - является ли баланс числом
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

"""
Все это очень неудобно, мы бы хотели получать баланас с помощью c.balance
А изменять его через присваивание, тут нам пригодится наш Property

"""

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значения
        return self.__balance

    def set_balance(self, value):# Поставит значение
        if not isinstance(value, (int, float)): # Проверка - является ли баланс числом
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):# удаляем баланс
        del self.__balance


    balance = property(fget=get_balance, fset=set_balance,fdel=delete_balance )# Создаем свойство, которое вернет наш экземпляр класса


""" К методу balance мы обращаемся не как к методу, а как к атрибуту"""
a = BankAccount('Misha', 400)
a.balance # ->400
a.balance = 999 # -> Баланс изменится
del a.balance # Баланс удалится 