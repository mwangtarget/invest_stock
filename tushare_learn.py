import tushare as ts
import sqlite3

conn = sqlite3.connect('invest_stock')
ts.set_token("73d044da8e0d5f08c5fe7050c8ea28a1cb9c72d4c88fb5e9c35fba60")
pro = ts.pro_api()

c = conn.cursor()
c.execute('''create table stock_all(state_dt varchar2(45),
                                          stock_code varchar2(45),
                                          open decimal(20,2),
                                          close decimal(20,2),
                                          high decimal(20,2),
                                          low decimal(20,2),
                                          vol int(20),
                                          amount decimal(30,2),
                                          pre_close decimal(20,2),
                                          amt_change decimal(20,2),
                                          pct_change decimal(20,2)) ''')


df = pro.daily(ts_code='603912.SH', start_date='20190610', end_date='20190614')

print(df)
