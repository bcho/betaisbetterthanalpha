#coding: utf-8

__all__ = ['get_report']


import re

_ = re.compile(u'(检查状况|查看报告)')


def get_report(c):
    return _.findall(c)
