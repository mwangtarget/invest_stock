import tushare as ts
import datetime
import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('invest_stock.db')
    ts.set_token("73d044da8e0d5f08c5fe7050c8ea28a1cb9c72d4c88fb5e9c35fba60")
    pro = ts.pro_api()

    c = conn.cursor()
    c.execute('''drop table stock_all''')
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

    start_dt = '20100101'
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')

    stock_pool = ['000725.SZ']
    total = len(stock_pool)

    for i in range(len(stock_pool)):
        try:
            df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
            print(df)
            print('Seq: ' + str(i + 1) + ' of ' + str(total) + '   Code: ' + str(stock_pool[i]))
            c_len = df.shape[0]
        except Exception as aa:
            print(aa)
            print('No DATA Code: ' + str(i))
            continue
        for j in range(c_len):
            resu0 = list(df.ix[c_len - 1 - j])
            resu = []
            for k in range(len(resu0)):
                if str(resu0[k]) == 'nan':
                    resu.append(-1)
                else:
                    resu.append(resu0[k])
            state_dt = (datetime.datetime.strptime(resu[1], "%Y%m%d")).strftime('%Y-%m-%d')
            try:
                sql_insert = "INSERT INTO stock_all(state_dt,stock_code,open,close,high,low,vol,amount,pre_close,amt_change,pct_change) VALUES ('%s', '%s', '%.2f', '%.2f','%.2f','%.2f','%i','%.2f','%.2f','%.2f','%.2f')" % (
                      state_dt, str(resu[0]), float(resu[2]), float(resu[5]), float(resu[3]), float(resu[4]), float(resu[9]),
                      float(resu[10]), float(resu[6]), float(resu[7]), float(resu[8]))
                c.execute(sql_insert)
                conn.commit()
            except Exception as err:
                 continue


    c.close()
    conn.close()
    print('All Finished!')


