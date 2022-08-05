"""Декоратор проперти
"""
""" Научимся использовать декоратор property
    Что это такое 
    x = property()
    x
Out[17]: <property at 0x2a2f5d4f950>  Свойство 
    x.getter(90) -> Тоже является свойством 
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

#       Мы все еще можем обращаться через переменные и через свойства
    my_balance = property(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)
