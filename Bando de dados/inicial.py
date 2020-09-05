from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, OptionProperty, NumericProperty, BooleanProperty, ReferenceListProperty, ListProperty, ObjectProperty, DictProperty # Usado para alterar o default de diversas propriedades
import mysql.connector
''' A lista acima carrega todas as bibliotecas usadas nesse programa'''

class Botao(Button): # Classe para customizar um tipo de botão com alguns parâmetros pré definidos. Não precisa de construtor. Estamos usando o pacote kivy.properties pra usar a classe dessa maneira.
    size_hint=ListProperty([1, .3])#[1,.4]
    background_color=ListProperty([0, .5,1,1])
    pos_hint=DictProperty({'center_x':.5,'center_y':.5})
    font_size=NumericProperty(30)   

class Rotulo(Label): # Classe para customizar um tipo de Label com alguns parâmetros pré definidos. Não precisa de construtor. Estamos usando o pacote kivy.properties pra usar a classe dessa maneira.
    size_hint=ListProperty([1, .3])
    background_color=ListProperty([0, .5,1,1])
    pos_hint=DictProperty({'center_x':.5,'center_y':.5})
    font_size=NumericProperty(20)
    bold=BooleanProperty(True)
    #halign= OptionProperty('left') 

class Inicio(BoxLayout): # Classe responsável pela criação da interface gráfica de acesso ao usuário.
    '''          self                                  self = BoxLayout - vertical
    -----------------------                        caixa A1 = BoxLayout - vertical
    |      caixa A1       |                        caixa A2 = GridLayout - 3 colunas
    -----------------------     -                  
    |     |       |       |                        
    |     |       |       |   
    |      caixa A2       |
    |     |       |       | 
    |     |       |       | 
    -----------------------     -
'''
    def __init__(self,*args,**kwargs):
        BoxLayout.__init__(self,*args,**kwargs)
        self.orientation='vertical'
        # widgets colocados na caixa (caixaA1>>caixa):
            
        self.caixaA1=BoxLayout(orientation='vertical',size_hint=(1,.30)) 
        self.titulo=Rotulo(text='Coop Estoque', font_size=30, size_hint=(1,.25),color=(1,1,1,.5));self.caixaA1.add_widget(self.titulo)     
        self.add_widget(self.caixaA1)

        # widgets colocados na caixaA2 (caixaA2>>caixa):

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
        self.cursor.execute(self.comando_SQL, self.usu)
        self.valores=self.cursor.fetchall() 
        ''' A sequência de comandos abaixo verifica se as informações digitadas pelo usuário estão de acordo com o banco de dados, caso contrário alguns avisos são enviados ao usuário'''
        if self.valores != []:
            if self.Isenha.text == self.valores[0][1]:
                self.Vusuario.text = ''
                self.Vsenha.text = 'Ok'
            else:
                self.Vusuario.text = ''
                self.Vsenha.text = 'Incorreta'
        else:
            self.Vusuario.text = 'Inexistente'

    def novo (self): # Ao ser chamada, essa função chama a função novo da classe principal (Principal()). 
        Principal.novo(self)

class Cadastro (BoxLayout): # Classe responsável pela criação da interface gráfica de cadastro do usuário. 
    def __init__(self,*args,**kwargs):
        BoxLayout.__init__(self,*args,**kwargs)
        self.orientation='vertical'
        self.a=(.35,.1)
        self.b=(.5, .1)
        self.c=(.15,.1)

        self.caixaA1=BoxLayout(orientation='vertical',size_hint=(1,.20)) 
        self.titulo=Rotulo(text='Cadastro', font_size=30, size_hint=(1,.15),color=(1,1,1,.5));self.caixaA1.add_widget(self.titulo)     
        self.add_widget(self.caixaA1)

        # Widgets inseridos na caixaA2 (caixaA2>>caixa):

        self.caixaA2=GridLayout(cols=3, spacing=10, size_hint=(1,.30))

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
                    Principal.inicio(self)

                else:
                    self.Vsalvar2.text='Senhas não conferem'
            else:
                self.Vsalvar2.text='Preencha todos os campos'
        else:
            self.Vsalvar2.text='Usuário já existe'
    
    def voltar(self): # Ao ser chamada, essa função chama a função início da classe principal (Principal()). 
        Principal.inicio(self)

class Principal(BoxLayout): # Classe que gerencia as mudanças de interface gráfica do aplicativo.
    def __init__(self,*args,**kwargs):
        BoxLayout.__init__(self,*args,**kwargs)
        self.orientation='vertical'
        
        self.tela=Inicio() # Define a classe Inicio() como um widget.
        self.add_widget(self.tela) # Insere a tela Inicio() como página inicial do app.
             
    def novo (self): # Ao ser chamada, essa função limpa a tela atual e abre a tela de cadastro de novo usuário.
        self.clear_widgets()
        self.tela=Cadastro() # Define a classe Inicio() como um widget
        self.add_widget(self.tela) # Insere a tela Inicio() como página inicial do app   
    
    def inicio (self): # Ao ser chamada, essa função limpa a tela atual e abre a tela de acesso do usuário.
        self.clear_widgets()
        self.tela=Inicio() # Define a classe Inicio() como um widget
        self.add_widget(self.tela) # Insere a tela Inicio() como página inicial do app   

class Janela(App): # classe que cria o núcleo do aplicativo e que chama a classe Principal() que gerenciará a troca de interfaces gráficas no aplicativo.
    def build(self):
        self.root=root=Principal()
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
