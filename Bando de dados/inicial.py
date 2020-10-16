from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, OptionProperty, NumericProperty, BooleanProperty, ReferenceListProperty, ListProperty, ObjectProperty, DictProperty # Usado para alterar o default de diversas propriedades
import mysql.connector
from kivy.uix.checkbox import CheckBox
''' A lista acima carrega todas as bibliotecas usadas nesse programa.'''

class Botao(Button): # Classe para customizar um tipo de botão com alguns parâmetros pré definidos. Não precisa de construtor. Estamos usando o pacote kivy.properties pra usar a classe dessa maneira.
    size_hint=ListProperty([1, .3])
    background_color=ListProperty([0, .5,1,1])
    pos_hint=DictProperty({'center_x':.5,'center_y':.5})
    font_size=NumericProperty(30)   

class Rotulo(Label): # Classe para customizar um tipo de Label com alguns parâmetros pré definidos. Não precisa de construtor. Estamos usando o pacote kivy.properties pra usar a classe dessa maneira.
    size_hint=ListProperty([1, .3])
    background_color=ListProperty([0, .5,1,1])
    pos_hint=DictProperty({'center_x':.5,'center_y':.5})
    font_size=NumericProperty(20)
    bold=BooleanProperty(True)

class Inicio(BoxLayout): # Classe responsável pela criação da interface gráfica de acesso ao usuário.
    def __init__(self,*args,**kwargs):
        BoxLayout.__init__(self,*args,**kwargs)
        '''A sequência de comandos abaixo cria cada elemento, junto com a sua localização, que é mostrado na interface gráfica apresentada ao usuário.'''
        self.orientation='vertical'   
        self.caixaA1=BoxLayout(orientation='vertical',size_hint=(1,.30)) 
        self.titulo=Rotulo(text='Coop Estoque', font_size=30, size_hint=(1,.25),color=(1,1,1,.5));self.caixaA1.add_widget(self.titulo)     
        self.add_widget(self.caixaA1)
        self.caixaA2=GridLayout(cols=3, spacing=10, size_hint=(1,.30))
        self.Lusuario=Rotulo(text='usuário:', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Lusuario)
        self.Iusuario=TextInput(text='',multiline=False, font_size=20,size_hint=(.4, .2), scroll_y=60);self.caixaA2.add_widget(self.Iusuario)
        self.Vusuario=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vusuario)
        self.Lsenha=Rotulo(text='senha:', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Lsenha)
        self.Isenha=TextInput(text='',password=True, multiline=False, font_size=20,size_hint=(.4,.2), scroll_y=60);self.caixaA2.add_widget(self.Isenha)
        self.Vsenha=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vsenha)
        self.Vir1=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vir1)
        self.Bir=Botao(text='IR',size_hint=(.4,.2), padding=(5,5)); self.caixaA2.add_widget(self.Bir)
        self.Vir2=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vir2) 
        self.Bir.on_press=self.conferir # Quando o botão "Ir" é clicado, a função conferir é chamada.
        self.Ventre1=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Ventre1)
        self.Ventre2=Rotulo(text='', size_hint=(.4,.2)); self.caixaA2.add_widget(self.Ventre2)
        self.Ventre3=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Ventre3)
        self.Vnovo1=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vnovo1)
        self.Bnovo=Botao(text='Novo usuário',size_hint=(.4,.2), background_color=(0, .5,1,.3), italic=True); self.caixaA2.add_widget(self.Bnovo)
        self.Vnovo2=Rotulo(text='', size_hint=(.3,.2)); self.caixaA2.add_widget(self.Vnovo2) 
        self.Bnovo.on_press=self.novo # Quando o botão "Novo usuário" é clicado, a função novo é chamada.     
        self.add_widget(self.caixaA2)
        self.Vazio=Rotulo(text='', size_hint=(1,.4)); self.add_widget(self.Vazio) 
    def conferir (self): # Abre o banco de dados e verifica se o que o usuário digitou condiz com os dados guardados no banco de dados.
        self.banco = mysql.connector.connect(host='localhost',user='root', password='', database='coop') # Conexão do Python com o banco de dados presente nas nuvens.
        self.cursor = self.banco.cursor()
        self.usu=self.Iusuario.text,
        self.comando_SQL ="SELECT * FROM cadastros where login = %s"
        self.cursor.execute(self.comando_SQL, self.usu) # Toda execução de comando em SQL será realizada dessa forma no Python.
        self.valores=self.cursor.fetchall() # Guarda os valores consultados no banco de dados em uma variável.
        ''' A sequência de comandos abaixo verifica se as informações digitadas pelo usuário estão de acordo com o banco de dados, caso contrário alguns avisos são enviados ao usuário'''
        if self.valores != []:
            if self.Isenha.text == self.valores[0][1]: # Se as informações fornecidas pelo usuário são verdadeiras, os comandos abaixo são executados.
                self.clear_widgets()
                self.tela=ConsultaBD(self.Iusuario.text) # O nome da tabela do usuário entra na classe ConsultaBD por aqui.  
                self.add_widget(self.tela) # Abre a tela ConsultaBD() como janela principal. 
            else: # Se as informações fornecidas pelo usuário não são corretas, as mensagens a seguir são exibidas na tela.
                self.Vusuario.text = ''
                self.Vsenha.text = 'Incorreta'
        else:
            self.Vusuario.text = 'Inexistente'
    def novo (self): # Ao ser chamada, essa função abre a tela de cadastro do usuário. 
        self.clear_widgets()
        self.tela=Cadastro()
        self.add_widget(self.tela) # Abre a tela Cadastro() como janela principal.   

class ConsultaBD (BoxLayout):
    def __init__(self,usu,*args,**kwargs):
        super(ConsultaBD, self).__init__(**kwargs)
        self.f = 15
        self.f2 = 17   
        self.nomeBD=usu
        self.orientation='vertical'
        self.Rteste=Rotulo(text='Consulta', size_hint=(1,.1)); self.add_widget(self.Rteste)
        self.caixaA1=GridLayout(cols=5, spacing=5, size_hint=(1,.3))
        self.legenda0=['Material','Preço (R$/kg)','Quantidade (kg)','Valor (R$)','Preço (R$/kg)']
        for i in range(5): # Criação da legenda da tabela de Consulta.
            self.legenda0[i]=Rotulo(text=self.legenda0[i],font_size=self.f); self.caixaA1.add_widget(self.legenda0[i])
        self.banco = mysql.connector.connect(host='localhost',user='root', password='', database='coop') # Conexão do Python com o banco de dados do usuário presente nas nuvens.
        self.cursor = self.banco.cursor()
        self.comando_SQL ="SELECT Material,Preço,Quantidade,(Preço*Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores=self.cursor.fetchall()
        self.n=len(self.valores)
        self.coluna=[]
        self.matr=[]
        for i in range(self.n): # criação de matriz de zeros
            for j in range(5):
                self.coluna.append(0)
            self.matr.append(self.coluna)
            self.coluna=[]
        for i in range(self.n): # criação de matriz com todos os elementos widgets da tabela de consulta
            for j in range(4):
                self.matr[i][j]=Rotulo(text=str(self.valores[i][j]),font_size=self.f2); self.caixaA1.add_widget(self.matr[i][j])
            self.matr[i][j+1]=TextInput(text=str(self.valores[i][j-2]),font_size=self.f2); self.caixaA1.add_widget(self.matr[i][j+1]) 
        self.vazio=Rotulo(text=''); self.caixaA1.add_widget(self.vazio)
        self.total=Rotulo(text='Total:',font_size=self.f2); self.caixaA1.add_widget(self.total)
        self.comando_SQL ="SELECT SUM(Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores2=self.cursor.fetchall()
        self.Qtotal=Rotulo(text=str(self.valores2[0][0]),font_size=self.f2); self.caixaA1.add_widget(self.Qtotal)
        self.comando_SQL ="SELECT SUM(Preço*Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores3=self.cursor.fetchall()
        self.Vtotal=Rotulo(text=str(self.valores3[0][0]),font_size=self.f2); self.caixaA1.add_widget(self.Vtotal)
        self.alterar=Botao(text="Alterar",font_size=self.f2); self.caixaA1.add_widget(self.alterar)
        self.alterar.on_press=self.calcular # Se o botão alterar for clicado, a função calcular é chamada para atualizar os valores de preço da tabela da Consulta.
        self.add_widget(self.caixaA1)
        '''A partir daqui o código é para a parte de entrada e saída de itens no estoque'''
        self.Rteste=Rotulo(text='Entrada/Saída', size_hint=(1,.1)); self.add_widget(self.Rteste)
        self.caixaA2=GridLayout(cols=5, spacing=10, size_hint=(1,.25))
        self.legenda=['','Material','Entrada(kg)','Saída(kg)','']
        for i in range(5):# Criação da legenda da tabela de Entrada/Saída.
            self.legenda[i]=Rotulo(text=self.legenda[i],font_size=self.f); self.caixaA2.add_widget(self.legenda[i])     
        self.matr2=[]
        for i in range(self.n): # criação de matriz de zeros
            for j in range(5):
                self.coluna.append(0)
            self.matr2.append(self.coluna)
            self.coluna=[]
        for i in range(self.n): # criação de matriz com todos os elementos widgets da tabela de entrada/saída
            self.matr2[i][0]=Rotulo(text='',font_size=self.f2); self.caixaA2.add_widget(self.matr2[i][0])
            self.matr2[i][1]=Rotulo(text=str(self.valores[i][0]),font_size=self.f2); self.caixaA2.add_widget(self.matr2[i][1])
            self.matr2[i][2]=TextInput(text='0.00',font_size=self.f2); self.caixaA2.add_widget(self.matr2[i][2])
            self.matr2[i][3]=TextInput(text='0.00',font_size=self.f2); self.caixaA2.add_widget(self.matr2[i][3])
            self.matr2[i][4]=Rotulo(text='',font_size=self.f2); self.caixaA2.add_widget(self.matr2[i][4])   
        self.add_widget(self.caixaA2)
        self.caixaA3=GridLayout(cols=3, padding=(30,5), size_hint=(1,.05))
        self.intera=['','Inserir','']
        self.intera[0]=Rotulo(text='');self.caixaA3.add_widget(self.intera[0])
        self.intera[1]=Botao(text='Inserir',font_size=self.f2);self.caixaA3.add_widget(self.intera[1])
        self.intera[2]=Rotulo(text='');self.caixaA3.add_widget(self.intera[2])
        self.add_widget(self.caixaA3)
        self.intera[1].on_press=self.calcular2 # Se o botão inserir for clicado, os valores da coluna Quantidade são atualizados e todas as demais colunas são atualizadas.
        self.temporario=Rotulo(text='',size_hint=(1,.2)); self.add_widget(self.temporario)
    def calcular(self): # Atualiza os valores do Preço da tabela de Consulta e recalcula todos os demais valores através da função calcula3.
        for i in range(self.n):
            self.matr[i][1].text=str(self.matr[i][4].text)
            self.comando_SQL ="UPDATE "+self.nomeBD+" SET Preço='"+self.matr[i][1].text+"' WHERE Material='"+self.matr[i][0].text+"'"  #fazer teste
            self.cursor.execute(self.comando_SQL)
        self.calcular3()
    def calcular2(self): # Atualiza os valores da coluna Quantidade da tabela de Consulta e recalcula todos os demais valores através da função calcula3.
        for i in range(self.n):
            self.quantid=float(self.matr[i][2].text)+float(self.matr2[i][2].text)-float(self.matr2[i][3].text)
            self.matr2[i][2].text='0.00'
            self.matr2[i][3].text='0.00'
            self.matr[i][2].text=str(self.quantid)
            self.comando_SQL ="UPDATE "+self.nomeBD+" SET Quantidade='"+self.matr[i][2].text+"' WHERE Material='"+self.matr[i][0].text+"'"  #fazer teste
            self.cursor.execute(self.comando_SQL)
        self.calcular3()
    def calcular3(self): # atualiza a tabela de consulta solicitada pelas funções calcular e calcular2.
        self.comando_SQL ="SELECT Material,Preço,Quantidade,(Preço*Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores=self.cursor.fetchall()
        for i in range(self.n): # criação de matriz com todos os elementos widgets da tabela de consulta
            for j in range(4):
                self.matr[i][j].text=str(self.valores[i][j])
            self.matr[i][j+1].text=str(self.valores[i][j-2])
        self.comando_SQL ="SELECT SUM(Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores2=self.cursor.fetchall()
        self.Qtotal.text=str(self.valores2[0][0])
        self.comando_SQL ="SELECT SUM(Preço*Quantidade) FROM "+self.nomeBD
        self.cursor.execute(self.comando_SQL)
        self.valores3=self.cursor.fetchall()
        self.Vtotal.text=str(self.valores3[0][0])
        self.banco.commit()

class Cadastro (BoxLayout): # Classe responsável pela criação da interface gráfica de cadastro do usuário. 
    def __init__(self,*args,**kwargs):
        BoxLayout.__init__(self,*args,**kwargs)
        self.orientation='vertical'
        self.a=(.35,.05)
        self.b=(.5, .05)
        self.c=(.15,.05)
        self.caixaA1=BoxLayout(orientation='vertical',size_hint=(1,.1)) 
        self.titulo=Rotulo(text='Cadastro', font_size=30, size_hint=(1,.05),color=(1,1,1,.5));self.caixaA1.add_widget(self.titulo)     
        self.add_widget(self.caixaA1)
        self.caixaA2=GridLayout(cols=3, spacing=10, size_hint=(1,.9))
        self.Lempresa=Rotulo(text='Empresa:', size_hint=self.a); self.caixaA2.add_widget(self.Lempresa)
        self.Iempresa=TextInput(text='',multiline=False, font_size=20,size_hint=self.b, scroll_y=60);self.caixaA2.add_widget(self.Iempresa)
        self.Vempresa=Rotulo(text='', size_hint=self.c); self.caixaA2.add_widget(self.Vempresa)
        self.Lendereco=Rotulo(text='Endereço eletrônico:', size_hint=self.a); self.caixaA2.add_widget(self.Lendereco)
        self.Iendereco=TextInput(text='',multiline=False, font_size=20,size_hint=self.b, scroll_y=60);self.caixaA2.add_widget(self.Iendereco)
        self.Vendereco=Rotulo(text='', size_hint=self.c); self.caixaA2.add_widget(self.Vendereco)
        self.Lusuario=Rotulo(text='Usuário:', size_hint=self.a); self.caixaA2.add_widget(self.Lusuario)
        self.Iusuario=TextInput(text='',multiline=False, font_size=20,size_hint=self.b, scroll_y=60);self.caixaA2.add_widget(self.Iusuario)
        self.Vusuario=Rotulo(text='', size_hint=self.c); self.caixaA2.add_widget(self.Vusuario)
        self.Lsenha=Rotulo(text='Senha:', size_hint=self.a); self.caixaA2.add_widget(self.Lsenha)
        self.Isenha=TextInput(text='',password=True, multiline=False, font_size=20,size_hint=self.b, scroll_y=60);self.caixaA2.add_widget(self.Isenha)
        self.Vsenha=Rotulo(text='', size_hint=self.c); self.caixaA2.add_widget(self.Vsenha)
        self.Lcsenha=Rotulo(text='Confirmar senha:', size_hint=self.a); self.caixaA2.add_widget(self.Lcsenha)
        self.Icsenha=TextInput(text='',password=True, multiline=False, font_size=20,size_hint=self.b, scroll_y=60);self.caixaA2.add_widget(self.Icsenha)
        self.Vcsenha=Rotulo(text='', size_hint=self.c); self.caixaA2.add_widget(self.Vcsenha)
        self.Vmateriais=Rotulo(text='',size_hint=self.a); self.caixaA2.add_widget(self.Vmateriais)
        self.Lmateriais=Rotulo(text='Materiais da cooperativa:',size_hint=self.b); self.caixaA2.add_widget(self.Lmateriais)
        self.Vmateriais2=Rotulo(text='',size_hint=self.c); self.caixaA2.add_widget(self.Vmateriais2)
        self.Lpapelao=Rotulo(text='Papelão:',size_hint=self.a);self.caixaA2.add_widget(self.Lpapelao)
        self.Cpapelao=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Cpapelao)
        self.Vpapelao=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Vpapelao)
        self.Lplastico=Rotulo(text='Plástico:',size_hint=self.a);self.caixaA2.add_widget(self.Lplastico)
        self.Cplastico=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Cplastico)
        self.Vplastico=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Vplastico)
        self.Lpapel=Rotulo(text='Papel:',size_hint=self.a);self.caixaA2.add_widget(self.Lpapel)
        self.Cpapel=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Cpapel)
        self.Vpapel=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Vpapel)
        self.Lvidro=Rotulo(text='Vidro:',size_hint=self.a);self.caixaA2.add_widget(self.Lvidro)
        self.Cvidro=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Cvidro)
        self.Vvidro=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Vvidro)
        self.Leletronicos=Rotulo(text='Eletrônicos:',size_hint=self.a);self.caixaA2.add_widget(self.Leletronicos)
        self.Celetronicos=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Celetronicos)
        self.Veletronicos=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Veletronicos)
        self.Laluminio=Rotulo(text='Alumínio:',size_hint=self.a);self.caixaA2.add_widget(self.Laluminio)
        self.Caluminio=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Caluminio)
        self.Valuminio=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Valuminio)
        self.Lborracha=Rotulo(text='Borracha:',size_hint=self.a);self.caixaA2.add_widget(self.Lborracha)
        self.Cborracha=CheckBox(size_hint=self.b);self.caixaA2.add_widget(self.Cborracha)
        self.Vborracha=Rotulo(text='',size_hint=self.c);self.caixaA2.add_widget(self.Vborracha)
        self.Vsalvar1=Rotulo(text='', size_hint=self.a); self.caixaA2.add_widget(self.Vsalvar1)
        self.Vsalvar2=Rotulo(text='', size_hint=self.b); self.caixaA2.add_widget(self.Vsalvar2) 
        self.Bsalvar=Botao(text='Salvar',size_hint=self.c, padding=(5,5), font_size=20); self.caixaA2.add_widget(self.Bsalvar)
        self.Bsalvar.on_press=self.salvar # Quando o botão "Salvar" é clicado, a função salvar é chamada. 
        self.Vvoltar1=Rotulo(text='', size_hint=self.a); self.caixaA2.add_widget(self.Vvoltar1)
        self.Vvoltar2=Rotulo(text='', size_hint=self.b); self.caixaA2.add_widget(self.Vvoltar2) 
        self.Bvoltar=Botao(text='Voltar',size_hint=self.c, padding=(5,5), font_size=20); self.caixaA2.add_widget(self.Bvoltar)
        self.Bvoltar.on_press=self.voltar # Quando o botão "Voltar" é clicado, a função voltar é chamada. 
        self.add_widget(self.caixaA2)
        self.Vazio=Rotulo(text='', size_hint=(1,.2)); self.add_widget(self.Vazio) 
    def salvar(self): # Salva o cadastro do usuário, caso o preenchimento dos dados tenha sido realizado adequadamente.
        self.banco = mysql.connector.connect(host='localhost',user='root', password='', database='coop') # Conexão do Python com o banco de dados presente nas nuvens.
        self.cursor = self.banco.cursor()
        self.usu=self.Iusuario.text,
        self.usu2=self.Iusuario.text
        self.comando_SQL ="SELECT * FROM cadastros where login = %s"
        self.cursor.execute(self.comando_SQL, self.usu)
        self.valores=self.cursor.fetchall() 
        ''' Os comandos acima abrem o banco de dados e fazem a consulta na tabela "cadastros"'''
        ''' A sequência de estruturas if abaixo, compara os dados inseridos pelo usuário e comparam com a tabela "cadastros" permitindo a inserção de um novo cadastro ou imprimindo alguma mensagem de inconsistência do usuário'''
        if self.valores == []:
            if self.Iempresa.text !='' and self.Iendereco.text !='' and self.Iusuario.text !='' and self.Isenha.text !='' and self.Icsenha.text !='':
                if self.Isenha.text == self.Icsenha.text:
                    self.comando_SQL = "INSERT INTO cadastros (login, senha, empresa, email) VALUES (%s,%s,%s,%s)"
                    self.dados = (self.Iusuario.text,self.Isenha.text,self.Iempresa.text,self.Iendereco.text)
                    self.cursor.execute(self.comando_SQL,self.dados)
                    self.banco.commit()
                    # O comando a seguir cria a tabela de estoque da cooperativa
                    self.comando_SQL = "CREATE TABLE "+self.Iusuario.text+"(Material VARCHAR(30) not null, Preço DECIMAL(5,2), Quantidade DECIMAL(6,3))"
                    self.cursor.execute(self.comando_SQL)
                    self.banco.commit()
                    # Os comandos abaixo alimentam o banco de dados do cliente com os materiais que são tratados na cooperativa                   
                    self.comando_SQL = "INSERT INTO "+self.Iusuario.text+ "(Material, Preço, Quantidade) VALUES (%s,0,0)"
                    if self.Cpapelao.active:
                        self.cursor.execute(self.comando_SQL,("Papelão",))
                    if self.Cplastico.active:
                        self.cursor.execute(self.comando_SQL,("Plástico",))
                    if self.Cpapel.active:
                        self.cursor.execute(self.comando_SQL,("Papel",))
                    if self.Cvidro.active:
                        self.cursor.execute(self.comando_SQL,("Vidro",))
                    if self.Celetronicos.active:
                        self.cursor.execute(self.comando_SQL,("Eletrônicos",))
                    if self.Caluminio.active:
                        self.cursor.execute(self.comando_SQL,("Alumínio",))
                    if self.Cborracha.active:
                        self.cursor.execute(self.comando_SQL,("Borracha",))
                    self.banco.commit()
                    self.clear_widgets()
                    self.tela=Inicio() # Define a classe Inicio() como um widget
                    self.add_widget(self.tela) # Insere a tela Inicio() como página inicial do app
                else:
                    self.Vsalvar2.text='Senhas não conferem'
            else:
                self.Vsalvar2.text='Preencha todos os campos'
        else:
            self.Vsalvar2.text='Usuário já existe'   
    def voltar(self): # Ao ser chamada, essa função chama a classe Início() de acesso ao usuário. 
        self.clear_widgets()
        self.tela=Inicio() # Define a classe Inicio() como um widget
        self.add_widget(self.tela) # Insere a tela Inicio() como página inicial do app 

class Janela(App): # classe que cria o núcleo do aplicativo e que chama a classe Principal() que gerenciará a troca de interfaces gráficas no aplicativo.
    def build(self):
        self.root=root=Inicio()
        root.bind(size=self._update_rect, pos=self._update_rect) # Dessa linha pra baixo (ateh self.rect.size=instance.size), o procedimento eh para criar um fundo colorido
        with root.canvas.before:
            Color(0,0,0,1)
            self.rect=Rectangle(size=root.size, pos=root.pos)
        self.title='Coop Estoque'
        return self.root
    def _update_rect(self,instance, value):
        self.rect.pos=instance.pos
        self.rect.size=instance.size
Janela().run() # Roda o aplicativo.
