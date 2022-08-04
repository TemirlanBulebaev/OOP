"""
Публичные, приватные, защищенные атрибуты и методы

"""
class BankAccount:

    def __init__(self, name, balance, passport):
        # self._name = name
        # self._balance = balance
        # self._passport = passport

         self.__name = name # Приватные переменные
         self.__balance = balance
         self.__passport = passport


    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport) Публичные переменные


    # def print_public_data(self): Второй вариант этой функции
    #     self.print_private_data()

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport) # Защищенные переменные,подчеркивания нужны по соглашению, лучше не использовать данные атрибуты вне класса

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 100000, 5000)
# account1.print_public_data()
# account1.print_protected_data() # Доступ все еще есть, подчеркивания нужны чтобы не использовать данный атрибут вне класса
account1.print_protected_data()

"""
Приватные переменные обозначаются двум __имя переменной, доступа к ним мы получить не можем, но можем обращаться внутри класса и вызывать метод с их использованием

"""

"""
Мы получаем доступ к приватным переменным через метод  - это называется:
    Инкапсуляция , т.е мы предоставляем пользователю метод по работе с нашими данными, через этот метод пользователь может получить доступ к зазизенным атрибутам
"""
account1.print_private_data()

print(dir(account1)) # функция покажет атрибуты
account1._BankAccount__print_private_date() # Так мы можем получить доступ к нашему методу

""" Переменные можно защитить с помощью специального модуля: accessify  Внутри него есть два декоратора протектид и превед"""