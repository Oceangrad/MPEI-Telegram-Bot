import requests
import logging as logger

from modules import config,scheduleparser

SECRET = config.SECRET

def getGroupByGroupName(groupName):
    return requests.get(SECRET.get('group_request_url',raw=True).format(groupName))
    
def getSchedule(groupId, weekStart, weekEnd):
    return requests.get(SECRET.get('schedule_search_request_url', raw=True)
                           .format(
                               groupId,
                               weekStart.strftime(scheduleparser.DATETIME_FORMAT),
                               weekEnd.strftime(scheduleparser.DATETIME_FORMAT)))