import configparser

# Загрузка конфигурации
config = configparser.ConfigParser()
config.read(filenames='config.ini',encoding="utf-8")

CUSTOM_MSG = config['CUSTOM.MESSAGES']
SECRET = config['SECRET']
DB_CREDS = config['SECRET.DATABASE']
DEFAULT_CONF = config['DEFAULT']