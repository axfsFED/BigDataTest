'''
Created on 2018年1月6日
主力净流入和股价，涨跌幅之间的关系统计
@author: lh159
'''

# 添加中文支持
from WindPy import *
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as ticker


if __name__ == '__main__':
    
    

    end_date = "2018-01-05"

    w.start()
    security_codes = w.weqs("新上市").Data[0]
    
    for security_code in ['002466.SZ']:
        #------------------------------------------------------------------------------获取上市日期
        _wss = w.wss(security_code, "ipo_date")
        start_date = _wss.Data[0][0].strftime("%Y-%m-%d")
        start_date = "2017-1-6"
        print(start_date)
        _wsd = w.wsd(security_code, "mfd_inflow_m,close,pct_chg",
                     start_date, end_date, "unit=1;Period=W;PriceAdj=F")
    
        mfd_inflow_m = [float(x) for x in _wsd.Data[0]]
        close = _wsd.Data[1]
        pct_chg = _wsd.Data[2]
        date = _wsd.Times
        
        print(date)
        #------------------------------------------------------------------------------画图
        # declare a figure object to plot
        fig = plt.figure()
        fig.gca(title=security_code)
        plt.xticks([])
        plt.yticks([])
    
        N = len(date)
        print(N)
        ind = np.arange(N) # the evenly spaced plot indices
        def format_date(x, pos=None):
            #保证下标不越界,很重要,越界会导致最终plot坐标轴label无显示
            thisind = np.clip(int(x+0.5), 0, N-1)
            return date[thisind].strftime('%Y-%m-%d')
    
        ax1 = fig.add_subplot(1, 1, 1)  # 创建子坐标图
    
        ax1.plot(ind, mfd_inflow_m, 'midnightblue', label="主力净流入", linewidth=1.2)
        plt.legend(loc='upper left')
        ax1.grid()
    
        ax2 = ax1.twinx()  # this is the important function，ax2作为ax1的兄弟坐标图
        ax2.plot(ind, close, 'darkred', label="股价", linewidth=1.2)
        plt.legend(loc='upper right')
        ax2.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    
        plt.gcf().autofmt_xdate()
        plt.show()
        # save the figure
        #plt.savefig(security_code+".png")

    pass
