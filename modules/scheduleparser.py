import logging as logger
import copy

from datetime import datetime, timedelta
from modules import config

DATETIME_FORMAT=config.DEFAULT_CONF.get("datetime_format",raw=True)
SCHEDULE_TEMP = {
    "Пн": [],
    "Вт": [],
    "Ср": [],
    "Чт": [],
    "Пт": [],
    "Сб": [],
    "Вс": [],
}
MONTHS = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]

# Преобразование запроса в словарь
def fromRequest(request):
    schedule = copy.deepcopy(SCHEDULE_TEMP)

    for lesson in request.json():
        schedule.get(lesson.get("dayOfWeekString")).append(lesson)

    return schedule

def getMonthStr(month):
    return MONTHS[month-1]

def parseDate(date):
    return datetime.strptime(date, DATETIME_FORMAT)

def getStartOfWeek():
    return datetime.today() - timedelta(days=datetime.today().weekday())

def getEndOfWeek():
    return getStartOfWeek() + timedelta(days=6)