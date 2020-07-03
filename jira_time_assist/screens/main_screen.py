import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.11.1")

class MainScreen(BoxLayout):
    url = ObjectProperty()
    username = ObjectProperty()
    password = ObjectProperty()


class MainApp(App):

    def build(self):
        Window.clearcolor = (.3, .3, .3, 1)
        return MainScreen()