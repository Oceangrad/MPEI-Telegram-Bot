"""МОДУЛИ ДЛЯ ПРОЕКТА МЭИ ИНФОБОТ"""

__version__ = "0.1"

import modules.scheduleparser as scheduleparser
import modules.dbquery as dbquery
import modules.config as config
import modules.requestquery as requestquery

import logging as logger

# Настройка логирования для отладки
logger.basicConfig(level=logger.getLevelName(config.DEFAULT_CONF['logging_level']))