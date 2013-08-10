#coding: utf-8

from ConfigParser import ConfigParser

import werobot


config = ConfigParser()
config.read('../config.ini')
TOKEN = config.get('wechat', 'token')

robot = werobot.WeRoBot(token=TOKEN)


@robot.subscribe
def subscribe(message):
    return message.content


@robot.text
def dispatch(message):
    return message.content
