""" Геттеры и сеттеры, property атрибуты
"""


class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport