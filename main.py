from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation


class Maid(App):
    def build(self):
        btn = Button(on_release=self.on)
        btn.size_hint = None, None
        btn.size = 300, 300
        btn.pos_hint = {"x": .30, "y": .3}
        btn.text = 'LIMPAR'
        btn.background_normal = '_imagens/circulo2.png'
        return btn

    def on(self, btn):
        box = BoxLayout()
        label = Label()
        label.text = 'testando'
        box.add_widget(label)


Maid().run()
