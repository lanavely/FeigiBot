import requests
from bs4 import BeautifulSoup as BS
from datetime import date


def get_schedule(group: str, scheduleDate: date):
    """Parses and returns the schedule"""
    r = requests.get("https://tt.chuvsu.ru/index/grouptt/gr/" + group)
    html = BS(r.content, 'html.parser')
    res = []
    td = html.find('td', attrs={'id': 'td' + scheduleDate.strftime('%Y%m%d') + 'g' + group})
    if td:
        for i in td.findAll('tr'):
            res.append(i.text + '\n')
    else:
        return 'Отсутсвует расписание на ' + scheduleDate.strftime('%d.%m.%Y')
    return ''.join(res)
