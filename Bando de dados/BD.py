import mysql.connector

banco = mysql.connector.connect(host='localhost',user='root', password='', database='coop')
cursor = banco.cursor()
#cursor.execute("CREATE DATABASE coop")

#cursor.execute("CREATE TABLE cadastros(login VARCHAR(20), senha VARCHAR(10), empresa VARCHAR(30), email VARCHAR(30))")


#comando_SQL = "INSERT INTO cadastros (login, senha, empresa, email) VALUES (%s,%s,%s,%s)"
#dados = ("recicla1","rec123","Mundo Recicla","recicla01@gmail.com")
#dados = ("recicla2","rec124","Global Recicla","grecicla@gmail.com")
#dados = ("ambientecoop","coop124","Cooperativa Ambiente","ambcoop@gmail.com")
#cursor.execute(comando_SQL,dados)
#banco.commit() # quando fizer alteração no banco de dados

#comando_SQL ="SELECT * FROM cadastros"
#cursor.execute(comando_SQL)
#valores_lidos=cursor.fetchall()
#print(valores_lidos[1][1]) # permite selecionar o item como se fosse uma matriz
#print(type(valores_lidos[1][1]))
#print(valores_lidos[1][1]=='rec124')

dado='recicla21'
dados=dado
comando_SQL ="SELECT senha FROM cadastros where login = %s"
cursor.execute(comando_SQL, (dado,))
valores_lidos=cursor.fetchall()
#print(valores_lidos[0][1]) # permite selecionar o item como se fosse uma matriz
print(valores_lidos)
print(valores_lidos==[])
print(type(valores_lidos))

''' No Mysql, 
para ver os bancos de dados: "show databases;", 
para ver a estrutura da tabela: "describe nome_tabela;", 
para mostrar todos os dados: "select * from nome_tabela;",
''' 
