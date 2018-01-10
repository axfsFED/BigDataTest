'''
Created on 2017年12月25日
【金融工程】统计显示，自2007年以来，近十年上证指数在最后五个交易日出现的涨跌各半，其中表现最好的是2014年最后五个交易日，涨幅高达8.82%。板块方面，银行、非银金融等权重板块常有相对不错的表现，成为最后一周稳定市场的主要力量。本周迎来2017年最后一个交易周，预期市场整体不会出现较大波动风险。仅供参考！
@author: lh159
'''

# 导入函数库
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码的问题
from WindPy import *  # 导入wind接口
import datetime
import time
import calendar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
import math
from sqlalchemy.types import String
from string import Template

#=========================================================================
# 统计标的（指数）在一定时间内的涨跌幅情况
# 输入：日期和标的（列表）
# 输出：标的（列表）涨跌幅
#=======================================================================


def stat(year, target):
    first_day = datetime.datetime(year, 1, 1)
    first_day_str1 = first_day.strftime("%Y-%m-%d")
    first_day_str2 = first_day.strftime("%Y%m%d")
    td_offset = w.tdaysoffset(-4, first_day,
                              "").Data[0][0].strftime("%Y%m%d")
    _wss = w.wss(target, "pct_chg_per, sec_name", "startDate=" +
                 td_offset + ";endDate=" + first_day_str2)
    return _wss.Data[0]


if __name__ == '__main__':
    w.start()
    # 获取所有申万一级行业指数
    _wset = w.wset("sectorconstituent","date=2017-12-25;sectorid=a39901011g000000")
    sw_industry_code = _wset.Data[1]
    sw_industry_name = _wset.Data[2]
    print(sw_industry_code)
    print(sw_industry_name)
    years = range(2008, 2018)
    pct_chg_per_list = []
    for y in years:
        pct_chg_per_list.append(stat(y, '801010.SI')[0])
    df = pd.DataFrame(index=[(y - 1) for y in years])
    df['pct_chg_per'] = pct_chg_per_list
    print(df)
    print(df['pct_chg_per'].describe())
    pass