'''
Created on 2018年1月4日
石化双雄拉升和大盘之间的关系
@author: lh159
'''

from sqlalchemy import Column, String, Integer, Float, create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import gevent

engine = create_engine(
    'sqlite:///BigData.db', echo=False)  # 创建数据库引擎


from WindPy import *  # 导入wind接口
import pandas as pd
if __name__ == '__main__':
    group = ["600028.SH", "601857.SH"]
    long_threshold = 3
    long_period = [5, 10, 20, 30, 60, 120, 240]
 
    start_date = "2007-11-04"
    end_date = "2018-01-03"
    
    tableName = '20180104'
# 
#     w.start()
#     _wsd = w.wsd(group, "pct_chg", start_date, end_date, "PriceAdj=F")
#     df = pd.DataFrame(_wsd.Data, index=_wsd.Codes, columns=_wsd.Times).T
#     df_filtered = df[(df[group[0]] > long_threshold) &
#                      (df[group[1]] > long_threshold)]
#     # print(df_filtered)
#     for p in long_period:
#         print(p)
#         pct_chg = []
#         for d in df_filtered.index:
#             d_1 = w.tdaysoffset(1, d, "").Data[0][0].strftime("%Y%m%d")
#             d_n = w.tdaysoffset(p, d, "").Data[0][0].strftime("%Y%m%d")
#             _wss = w.wss("000001.SH", "pct_chg_per","startDate="+d_1+";endDate="+d_n)
#             pct_chg.append(_wss.Data[0][0])
#         df_filtered["pct_chg_"+str(p)] = pct_chg
#     print(df_filtered)
#     print(df_filtered.describe())
#     df_filtered.to_sql('20180104', engine, if_exists='replace', index=True)

    df = pd.read_sql(tableName, engine)
    print(df.describe())
    ratio_up_list = []
    for p in long_period:
        pct_chg_list = list(df["pct_chg_"+str(p)])
        ratio_up = round(sum([1 if pct_chg > 0 else 0 for pct_chg in pct_chg_list])/len(pct_chg_list)+0.00001, 4)*100
        ratio_up_list.append(ratio_up)
    print(ratio_up_list)
    pass