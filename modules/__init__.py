"""МОДУЛИ ДЛЯ ПРОЕКТА МЭИ ИНФОБОТ"""

import modules.scheduleparser as scheduleparser
import modules.dbquery as dbquery
import modules.config as config
import modules.requestquery as requestquery

import logging as logger

__version__ = config.DEFAULT_CONF['version']

# Настройка логирования для отладки
logger.basicConfig(level=logger.getLevelName(config.DEFAULT_CONF['logging_level']))