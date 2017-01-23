__author__ = 'FrankLin'

import sqlite3
class SQLite:

    def QueryToList(sSql,sDBName):
        #宣告CONN跟CURS
        conn = sqlite3.connect(sDBName)  #相對位置
        curs = conn.cursor()

        #執行SQL語法
        curs.execute(sSql)

        lstTemp = []
        #用迴圈讀取
        for s in curs.fetchall():
            lstTemp.append(s)

        #關閉資料庫連接
        curs.close()
        conn.close()

        return lstTemp

    def QueryValue(sSql,sDBName):
        #宣告CONN跟CURS
        conn = sqlite3.connect(sDBName)  #相對位置
        curs = conn.cursor()
        #執行SQL語法
        curs.execute(sSql)
        sTemp = ""
        sTemp = curs.fetchone()

        #關閉資料庫連接
        curs.close()
        conn.close()

        return sTemp