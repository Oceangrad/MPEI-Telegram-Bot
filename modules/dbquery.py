import psycopg2
import logging as logger

from modules import config

conn = None
cursor = None

# Запрос на подключение к БД
def connect():
    global conn,cursor

    credentials = config.DB_CREDS

    logger.info("Подключение к БД...")

    conn = psycopg2.connect(
        host=credentials['host'],
        port=credentials['port'],
        dbname=credentials['dbname'],
        user=credentials['user'],
        password=credentials['password'])

    cursor = conn.cursor()

    logger.info("Успешно подключено к БД")

def findUserByUserId(userId):
    cursor.execute("SELECT * FROM users WHERE user_id=%s;", (userId,))
    return cursor.fetchone()

def addNewUser(userId, groupName):
    cursor.execute("INSERT INTO users (user_id, student_group) VALUES (%s, %s);", (userId, groupName))
    conn.commit()

def updateUserGroup(userId, groupName):
    cursor.execute("UPDATE users SET student_group = %s WHERE user_id = %s;", (groupName, userId))
    conn.commit()