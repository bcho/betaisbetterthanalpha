#coding: utf-8

__all__ = ['get_report', 'report_not_found']


def get_report(value):
    return u'现在的环境温度：%(t)s  湿度: %(h)s  '
    '固体颗粒物浓度： %(pm)s  甲醛气体浓度： %(ch)s' % value


def report_not_found():
    return u'暂时没有报告哦'
