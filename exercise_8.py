from datetime import datetime
from datetime_print import print_date, print_datetime
from datetime_print.time_print import print_time

now = datetime.now()
print_date(now)
print_time(now)
print_datetime(now)
