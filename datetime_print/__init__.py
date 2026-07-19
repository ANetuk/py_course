from datetime import datetime
from .time_print import print_time

def print_date(dt: datetime):
    print(f'{dt: %d.%m.%Y}')

def print_datetime(dt: datetime):
    print_date(dt)
    print_time(dt)
