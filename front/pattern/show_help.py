#coding: utf-8

__all__ = ['show_help']


import re

_ = re.compile(u'^(查看帮助|help|h)')


def show_help(c):
    return _.findall(c)
