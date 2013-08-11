#coding: utf-8

__all__ = ['send_ir']


import re

_ = re.compile(u'^(切换投影仪)')


def send_ir(c):
    return _.findall(c)
