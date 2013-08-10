#coding: utf-8

__all__ = ['get_report', 'report_not_found']


def get_report(value):
    return u'现在的环境温度：%(t)  湿度: %(h)  '
    '固体颗粒物浓度： %(pm)  甲醛气体浓度： %(ch)' % value


def report_not_found():
    return u'暂时没有报告哦'
