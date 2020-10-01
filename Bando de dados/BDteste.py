import mysql.connector

banco = mysql.connector.connect(host='localhost',user='root', password='')
cursor = banco.cursor()
#cursor.execute("CREATE DATABASE teste2")
cursor.execute("use teste2")
dado='bananao'
#dado.replace("'","")
#print(dado)
#print(type(dado))

comando_SQL ="CREATE TABLE "+dado+"(login VARCHAR(20), senha VARCHAR(10), empresa VARCHAR(30), email VARCHAR(30))"
#comando_SQL2 ="(login VARCHAR(20), senha VARCHAR(10), empresa VARCHAR(30), email VARCHAR(30))"
#comando_SQL ="CREATE TABLE '%s'(login VARCHAR(20), senha VARCHAR(10), empresa VARCHAR(30), email VARCHAR(30))"
#omando_SQL=comando_SQL1+dado+comando_SQL2
print(comando_SQL)
cursor.execute(comando_SQL)

'''
#comando_SQL = "INSERT INTO cadastros (login, senha, empresa, email) VALUES (%s,%s,%s,%s)"
#dados = ("recicla1","rec123","Mundo Recicla","recicla01@gmail.com")
#dados = ("recicla2","rec124","Global Recicla","grecicla@gmail.com")
#dados = ("ambientecoop","coop124","Cooperativa Ambiente","ambcoop@gmail.com")
#cursor.execute(comando_SQL,dados)
#banco.commit() # quando fizer alteração no banco de dados'''