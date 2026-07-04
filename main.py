import asyncio
import logging as logger

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from modules import *

# Подключение конфигурации
CUSTOM_MSG = config.CUSTOM_MSG
DEFAULT_CONFIG = config.DEFAULT_CONF

# Инициализация подключения к БД
dbquery.connect()
# dasf
# Инициализация бота и диспетчера
bot = Bot(token=config.SECRET['token'])
dp = Dispatcher()

# Обработчики событий
@dp.message(Command("r"))
async def cmd_raspisanie(message: types.Message):
    
    # Валидация введенной группы
    groupName = message.text.replace("/r", "").upper().strip()

    if (len(groupName) == 0):
        db_user = dbquery.findUserByUserId(message.from_user.id)

        if (dbquery.cursor.rowcount == 0):
            await message.answer(CUSTOM_MSG['cmd_raspisanie_no_group_error'])
            return
        
        groupName = db_user[2].upper().strip()

    response = requestquery.getGroupByGroupName(groupName)

    if (len(response.json()) == 0):
        await message.answer(CUSTOM_MSG['no_group_found_error'])
        await message.answer(CUSTOM_MSG['input_group_warn'].format("/r"))
        
        return

    # Заполнение строки ответа
    answer = CUSTOM_MSG['schedule_title'].format(groupName)
    answer += "\n\n"

    groupId = response.json()[0].get("id", -1)
    weekStart = scheduleparser.getStartOfWeek()
    weekEnd = scheduleparser.getEndOfWeek()

    response = requestquery.getSchedule(groupId, weekStart, weekEnd)
    schedule = scheduleparser.fromRequest(response)

    for day in dict.items(schedule):

        dayName = day[0]
        lessons = day[1]

        if (len(lessons) == 0):
            continue

        currentDate = scheduleparser.parseDate(lessons[0].get("date"))
        answer += f"{dayName.upper()} {currentDate.day} {scheduleparser.getMonthStr(currentDate.month)}\n"

        for lesson in lessons:
            answer += f"{lesson.get('beginLesson')} - {lesson.get('endLesson')} {lesson.get('discipline')}\n"
            
        answer += "\n"

    answer += CUSTOM_MSG.get("schedule_addition",raw=True)

    await message.answer(answer, parse_mode="HTML")
    await message.answer(CUSTOM_MSG['schedule_info'], parse_mode="HTML")

@dp.message(Command("group"))
async def cmd_set_group(message: types.Message):

    # Валидация группы
    groupName = message.text.replace("/group", "").upper().strip()

    if (len(groupName) == 0):
        await message.answer(CUSTOM_MSG['input_group_warn'].format("/group"), parse_mode="HTML")
        return

    response = requestquery.getGroupByGroupName(groupName)

    if (len(response.json()) == 0):
        await message.answer(CUSTOM_MSG['no_group_found_error'])
        await message.answer(CUSTOM_MSG['input_group_warn'].format("/group"))

        return

    # Добавление/Изменение группы пользователя
    db_user = dbquery.findUserByUserId(message.from_user.id)

    if (dbquery.cursor.rowcount == 0):
        dbquery.addNewUser(message.from_user.id, groupName)
        await message.answer(CUSTOM_MSG['set_group_success'].format(groupName))

        return

    if (db_user[2].upper().strip() == groupName):
        await message.answer(CUSTOM_MSG['group_already_set_error'])
        return

    dbquery.updateUserGroup(message.from_user.id, groupName)

    await message.answer(CUSTOM_MSG['set_group_success'].format(groupName))

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_start'], parse_mode="HTML")

@dp.message(Command("materiali"))
async def cmd_materiali(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_materiali'])

@dp.message(Command("official"))
async def cmd_official(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_official'])

@dp.message(Command("osep"))
async def cmd_osep(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_osep'])

@dp.message(Command("bars"))
async def cmd_bars(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_bars'])

@dp.message(Command("lektsii"))
async def cmd_lektsii(message: types.Message):
    await message.answer(CUSTOM_MSG['cmd_lektsii'])

# Запуск бота
@dp.startup()
async def bot_startup():
    logger.info("Бот успешно запущен!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logger.info("Бот запускается...")
    logger.debug("Debugging Mode")
    asyncio.run(main())
