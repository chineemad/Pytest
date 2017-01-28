__author__ = 'FrankLin'
import MyDBCommand

#======================================

sDBName = "DB.sqlite"
sSql = "SELECT * FROM stores WHERE address like '%台南市%'"

for s in MyDBCommand.SQLite.QueryToList(sSql,sDBName):
    print(s)

sSql = "SELECT address FROM stores WHERE address like '%台南市%'"
print(MyDBCommand.SQLite.QueryValue(sSql,sDBName))

sSql = "SELECT address FROM stores "
print(MyDBCommand.SQLite.QueryValue(sSql,sDBName))