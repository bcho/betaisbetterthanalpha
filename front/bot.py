#coding: utf-8

import werobot

from config import TOKEN

robot = werobot.WeRoBot(token=TOKEN)


@robot.subscribe
def subscribe(message):
    return message.content


@robot.text
def dispatch(message):
    return message.content
