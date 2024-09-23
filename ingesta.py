import mysql.connector
import csv 

mydb = mysql.connector.connect(
  host="34.200.117.75",
  port=8005,
  user="root",
  password="utec",
  database="tienda"
)
print(mydb)
dbQuery='SELECT * FROM fabricantes;'

cursor = mydb.cursor()
cursor.execute(dbQuery)
rows = cursor.fetchall()
fp = open('fabricantes.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()