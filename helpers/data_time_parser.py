import datetime
from helpers import next_day_of_week_date

tomorrow = ['на завтра', 'завтра', 'зав', 'з']
mon = ['понедельник', 'пн']
tue = ['вторник', 'вт']
wed = ['среда', 'ср']
thu = ['четверг', 'чт']
fri = ['пятница', 'пт']
sat = ['суббота', 'сб']
sun = ['воскресенье', 'вс']


def get_date_by_name(text : str) -> datetime:
    text.strip().lower()
    day_of_week = datetime.datetime.today().weekday()
    if text in tomorrow:
        day_of_week = day_of_week + 1 if day_of_week != 7 else 1
    if text in mon:
        day_of_week = 0
    if text in tue:
        day_of_week = 1
    if text in wed:
        day_of_week = 2
    if text in thu:
        day_of_week = 3
    if text in fri:
        day_of_week = 4
    if text in sat:
        day_of_week = 5
    if text in sun:
        day_of_week = 6
    return next_day_of_week_date.get_next_day_of_week_date(day_of_week)