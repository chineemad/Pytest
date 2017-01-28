__author__ = 'FrankLin'
import MyDBCommand

#======================================
'''
sDBName = "DB.sqlite"
sSql = "SELECT * FROM stores WHERE address like '%台南市%'"

for s in MyDBCommand.SQLite.QueryToList(sSql,sDBName):
    print(s)

sSql = "SELECT address FROM stores WHERE address like '%台南市%'"
print(MyDBCommand.SQLite.QueryValue(sSql,sDBName))
'''
#---------------------------------------------

import numpy as np
import pandas as pd
#url = 'http://www.stockq.org/market/asia.php'
#pd.read_html(url)[4]

#print(pd)

data = np.random.randn(10,5)
#print(data)
df = pd.DataFrame(data, columns=list("ABCDE"))
print(df)
print(df[1:4])
print(df[["A"]])

print(df.plot())