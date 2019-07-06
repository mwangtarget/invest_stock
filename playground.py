import tushare as ts
import datetime
import sqlite3

if __name__ == '__main__':
    ts.set_token("73d044da8e0d5f08c5fe7050c8ea28a1cb9c72d4c88fb5e9c35fba60")
    pro = ts.pro_api()
    #df = pro.stock_basic(exchange='SSE', list_status='L', fields='ts_code, symbol,name,area,industry,list_date')

    #print(df['list_date'].min())
    #print(df.sort_values(by=['list_date'], ascending=True))

    #Get daily quote
    #df_fr = pro.daily(ts_code='600612.SH', start_date='20170515', end_date='20180721')
    #print(df_fr)


    #Get trading calendar
    #df_cal = pro.trade_cal(exchange='', start_date='20180101', end_date='20181231')
    #print(df_cal)

    #Get 成分股
    #df_cons = pro.hs_const(hs_type='SH')
    #print(df_cons)

    #Get Shibor rate
    # 2013-06 流动性危机
    # 2009 大水漫灌
    df_shibor = pro.shibor(start_date='20090501', end_date="20090630")
    print(df_shibor)