import datetime


def get_next_day_of_week_date(day_of_week: int) -> datetime:
    day_difference = day_of_week - datetime.datetime.today().weekday();
    if day_difference < 0:
        day_difference = 7 + day_difference;
    return datetime.datetime.today() + datetime.timedelta(days=day_difference);
