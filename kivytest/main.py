#!/usr/bin/env python3

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy import require
require('2.1.0')


class MainWindow(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainWindow()


app = MainApp()
app.run()
