import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial


class MainWindow(App):
    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = "I am Disabled!"

    def build(self):
        button = Button(text="Click me to disable", pos=(300, 350), size_hint=(.25, .18))
        button.bind(on_press=partial(self.disable, button))
        button.bind(on_press=partial(self.update, button))
        return button


if __name__ == '__main__':
    MainWindow().run()
