#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window;

class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)
		value = StringProperty()
		
	def fc1(self):
		#self.ids.lb5.value += self.value
		self.ids.lb5.value += "Teste bem sucedido!\n"
	def fc2(self):
		self.ids.lb5.value += "Também funcionou!\n"
		self.ids.lb10.pedido += 10	
class MyLabel(Label):
	value = StringProperty()
	#pedido = NumericProperty(0)

class MyLabel2(Label):
	pedido = NumericProperty(0)

class RootScreen(ScreenManager):
    pass
class dinamicoApp(App):
	title = 'Scrollview dinamico!!'
	
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = dinamicoApp()
    dinamicoApp().run()

