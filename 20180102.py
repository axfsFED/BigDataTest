'''
Created on 2018年1月2日
统计每年首日涨跌和全年涨跌之间的关系
【安赢汇-大数据】统计显示，自1991年至2017年共计27年间，上证指数首日上涨的概率为62.96%，首日上涨的情况下，全年上涨的概率为58.82%，首日涨跌幅和全年涨跌幅的相关系数为0.203，呈现一定程度正相关；自2003年至2017年共计15年间，沪深300首日上涨的概率为60%，首日上涨的情况下，全年上涨的概率为55.56%，首日涨跌幅和全年涨跌幅的相关系数为0.338，呈现一定程度正相关；仅供参考！
@author: lh159
'''
from WindPy import *  # 导入wind接口
import datetime
import time
import pandas as pd

if __name__ == '__main__':
    w.start()
    target_security = "000300.SH"
    years = range(2003, 2018)
    df = pd.DataFrame(index=years)
    first_trade_date_pct_chg = []
    full_year_pct_chg = []
    for y in years:
        first_date = datetime.datetime(y, 1, 1).strftime("%Y-%m-%d")
        first_trade_date = w.tdaysoffset(
            1, first_date, "").Data[0][0].strftime("%Y%m%d")
        _wss = w.wss(target_security, "pct_chg", "tradeDate=" +
                     first_trade_date + ";cycle=D")
        first_trade_date_pct_chg.append(_wss.Data[0][0])
    df['first_trade_date_pct_chg'] = first_trade_date_pct_chg
    _wsd = w.wsd(target_security, "pct_chg", "2003-01-01",
                 "2018-01-01", "Period=Y;PriceAdj=F")
    df['full_year_pct_chg'] = _wsd.Data[0]
    print(df)
    print(df.describe())
    corr = df['first_trade_date_pct_chg'].corr(df['full_year_pct_chg'])
    print("首日和全年的相关系数为：%f" % corr)
    print("首日上涨的概率为：%f" % (sum(
        [1 for chg in first_trade_date_pct_chg if chg > 0]) / len(first_trade_date_pct_chg)))
    
    df_new = pd.DataFrame(index=years)
    df_new['first_trade_date_pct_chg'] = [1 if chg > 0 else 0 for chg in first_trade_date_pct_chg ]
    df_new['full_year_pct_chg'] = [1 if chg > 0 else 0 for chg in _wsd.Data[0]] 
    print(df_new)
    corr = df_new['first_trade_date_pct_chg'].corr(df_new['full_year_pct_chg'])
    print("首日和全年的相关系数为(涨跌)：%f" % corr)
    df_filtered = df_new[df_new['first_trade_date_pct_chg']==1]
    print(df_filtered)
    up_ratio = sum(list(df_filtered['full_year_pct_chg']))/len(list(df_filtered['full_year_pct_chg']))
    print("首日上涨，全年上涨的概率为：%f" % up_ratio)
    pass
