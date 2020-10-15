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

coluna = []
matriz = []

for i in range(3):
    for j in range(5):
        coluna.append(0)
    matriz.append(coluna)
    coluna=[]
#print(matriz)
#matriz[0][1]=3
#print(matriz)

x=matriz

x[0][0]=4

#print(x)
#print(matriz)

matriz[0][1]=8

#print(x)
#print(matriz)