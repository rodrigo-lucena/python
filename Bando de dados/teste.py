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
''' A lista acima carrega todas as bibliotecas usadas nesse programa'''
import Cadastro
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

        self.caixaA2=GridLayout(cols=2, spacing=10, size_hint=(1,.30))
        self.x=2 #colunas
        self.y=3 #linhas
        self.matriz=[self.x*[0]]*self.y
        print(self.matriz)
        print(self.matriz[2][0])
        

        self.matriz[0][0]=Rotulo(text='teste', size_hint=(.3,.2)); self.caixaA2.add_widget(self.matriz[0][0])
        self.matriz[0][1]=Rotulo(text='teste2', size_hint=(.3,.2)); self.caixaA2.add_widget(self.matriz[0][1])
        self.matriz[1][0]=Rotulo(text='teste3', size_hint=(.3,.2)); self.caixaA2.add_widget(self.matriz[1][0])
        self.matriz[1][1]=Rotulo(text='teste4', size_hint=(.3,.2)); self.caixaA2.add_widget(self.matriz[1][1])
        
        self.caixaA1.add_widget(self.caixaA2)
        




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
