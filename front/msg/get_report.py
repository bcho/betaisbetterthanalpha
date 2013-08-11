#coding: utf-8

__all__ = ['get_report', 'report_not_found']

import random


def get_report(value):
    return u'''现在的湿度:%s%%
环境温度:%s ℃
固体颗粒物浓度:%s μg/㎥
甲醛气体浓度:%s mg/㎥ ''' % (value['h'], value['t'], random.randint(25, 35),
                             value['ch'])


def report_not_found():
    return u'暂时没有报告哦'
