import kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
Window.size = (600,600)

class WindowTabbedPanel(TabbedPanel):
    pass

class PySoundboardApp(App):
    def build(FloatLayout):
        pass

PySoundboardApp().run()