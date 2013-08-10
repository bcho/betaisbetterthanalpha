#coding: utf-8

import werobot

from config import TOKEN

import msg
import pattern
import action

robot = werobot.WeRoBot(token=TOKEN)


@robot.subscribe
def subscribe(message):
    return msg.subscribe()


@robot.text
def dispatch(message):
    content = message.content.strip()
    if not isinstance(content, unicode):
        content = content.decode('utf-8')

    if pattern.show_help(content):
        return msg.show_help()

    # turn on/off
    op, obj = pattern.op(content)
    if op and obj:
        if action.op(op, obj):
            return msg.op(op, obj)
        else:
            return msg.op_failed(op, obj)

    # get report
    if pattern.get_report(content):
        return action.get_report()

    return msg.show_help()
