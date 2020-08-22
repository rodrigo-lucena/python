import mysql.connector

cnx = mysql.connector.connect(host='localhost',user='root', password='')

cnx.close()
