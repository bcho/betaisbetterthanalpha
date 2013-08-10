#coding: utf-8

import werobot

from config import TOKEN

import msg

robot = werobot.WeRoBot(token=TOKEN)


@robot.subscribe
def subscribe(message):
    return msg.subscribe()


@robot.text
def dispatch(message):
    if message.content == 'help':
        return msg.show_help()
