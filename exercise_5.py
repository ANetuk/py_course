from decimal import Decimal
from typing import Literal
import random

class Person:
    def __init__(self, tin: str):
        self.__tin = tin

    def get_tin(self):
        return self.__tin

    def get_full_name(self):
        pass

class SoleProprietor(Person):
    def __init__(self, tin: str, first_name: str, last_name: str, middle_name: str, activities: list[str]):
        super().__init__(tin)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__activities = activities

    def get_full_name(self):
        return f'{self.__first_name} {self.__last_name} {self.__middle_name}'

    def get_activities_string(self):
        return ', '.join(self.__activities)

class LegalEntity(Person):
    def __init__(self, tin: str, legal_form: Literal['LLC', 'JSC', 'PJSC'], name: str):
        super().__init__(tin)
        self.__legal_form = legal_form
        self.__name = name

    def get_legal_form(self):
        if self.__legal_form == 'LLC':
            return 'ООО'
        if self.__legal_form == 'JSC':
            return 'АО'
        if self.__legal_form == 'PJSC':
            return 'ПАО'
        return 'Другая форма организации'

    def get_full_name(self):
        legal_form = self.get_legal_form()
        return f'{legal_form} {self.__name}'

class Document:
    def __init__(self, name: str, number: str, date: str, person: Person):
        self.__name = name
        self.__number = number
        self.__date = date
        self.__person = person

    def get_title(self):
        return f'{self.__name} №{self.__number} от {self.__date}'

    def get_person_tin(self):
        return self.__person.get_tin()

    def get_person_full_name(self):
        return self.__person.get_full_name()

    def set_person(self, person: Person):
        self.__person = person

class CheckbookRequest(Document):
    def __init__(self, number: str, date: str, person: Person, series: str, first_check_number: int, pages_count: int):
        super().__init__('Заявление на получение чековой книжки', number, date, person)
        self.__series = series
        self.__first_check_number = first_check_number
        self.__pages_count = pages_count

    def get_last_check_number(self):
        return self.__first_check_number + self.__pages_count - 1

    def get_checkbook_title(self):
        last_check_number = self.get_last_check_number()
        return f'Чековая книжка {self.__series} №№{self.__first_check_number} - {last_check_number}'

class CashSymbol:
    def __init__(self, name: str, amount: Decimal, priority: int):
        self.__name = name
        self.__amount = amount
        self.__priority = priority

    def get_name(self):
        return self.__name

    def get_priority(self):
        return self.__priority

    def get_amount(self):
        return self.__amount

class CashPayoutRequest(Document):
    def __init__(self, number: str, date: str, person: Person, cash_symbols: list[CashSymbol]):
        super().__init__('Заявление на получение наличных денег', number, date, person)
        self.__cash_symbols = cash_symbols

    def get_priority(self):
        symbol_priorities = [symbol.get_priority() for symbol in self.__cash_symbols]
        return min(symbol_priorities)

    def get_amount(self):
        symbol_amounts = [symbol.get_amount() for symbol in self.__cash_symbols]
        return sum(symbol_amounts)

sole_proprietor = SoleProprietor(
    '771234567890',
    'Иванов',
    'Иван',
    'Иванович',
    ['Разработка компьютерного программного обеспечения', 'Деятельность по обработке данных']
)

checkbook_request = CheckbookRequest(
    '1',
    '13.07.2026',
    sole_proprietor,
    'АА',
    1,
    25
)

print(checkbook_request.get_person_tin())
print(checkbook_request.get_person_full_name())

legal_entity = LegalEntity('7701234567', 'LLC', 'Рога и копыта')
checkbook_request.set_person(legal_entity)

print(checkbook_request.get_person_tin())
print(checkbook_request.get_person_full_name())

# Задание 1
# Базовый класс Document включает в себя поле с типом Person.
# Методы Document get_person_tin и get_person_full_name делегируют работу методам person.
# Реализация get_person_full_name зависит от типа SoleProprietor или LegalEntity

# Задание 2
# Полиморфизм подтипов - это когда метод, который должен быть вызван выбирается в зависимости от типа объекта.
# То есть клиент знает о внешнем интерфейсе - наличии определенного метода, и просто работает с ним,
# а реализация выбирается уже в зависимости от типа объекта.
# Параметрический полиморфизм - это когда один и тот же код функции может корректно работать с переменными разных типов.
# Например, код работы со списками может работать одинаково,
# несмотря на то, что в списке могут быть значения разных типов.

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def clear_and_fill_animals(animals: list[Animal]):
    animals.clear()
    for _ in range(500):
        new_animal = random.choice([Cat(), Bird()])
        animals.append(new_animal)

animals = []
clear_and_fill_animals(animals)
for animal in animals:
    animal.foo()

# Задание 3
# Получается, что массив animals содержит 500 элементов типа Cat или Bird,
# Клиент просто вызывает foo, а в зависимости от типа уже выбирается реализация Cat.foo или Bird.foo
