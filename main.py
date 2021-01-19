from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Maid(App):
    def build(self):
        box = BoxLayout()
        btn = Button(text='hello')
        box.add_widget(btn)
        return box


Maid().run()
