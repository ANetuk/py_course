from decimal import Decimal
from typing import Literal

class Person:
    def __init__(self, tin: str):
        self.__tin = tin

    def get_tin(self):
        return self.__tin

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
print(sole_proprietor.get_tin())
print(sole_proprietor.get_full_name())
print(sole_proprietor.get_activities_string())

legal_entity = LegalEntity('7701234567', 'LLC', 'Рога и копыта')
print(legal_entity.get_legal_form())
print(legal_entity.get_full_name())

checkbook_request = CheckbookRequest(
    '1',
    '13.07.2026',
    sole_proprietor,
    'АА',
    1,
    25
)
print(checkbook_request.get_title())
print(checkbook_request.get_last_check_number())
print(checkbook_request.get_checkbook_title())

cash_payout_request = CashPayoutRequest(
    '1',
    '13.07.2026',
    legal_entity,
    [
        CashSymbol('Выдача заработной платы', Decimal(1000), 3),
        CashSymbol('Другие выплаты', Decimal(200), 5)
    ]
)
print(cash_payout_request.get_amount())
print(cash_payout_request.get_priority())
