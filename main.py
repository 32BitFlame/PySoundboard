import kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.button import Button
Window.size = (600,600)

class WindowTabbedPanel(TabbedPanel):
    pass

class PySoundboardApp(App):
    def build(FloatLayout):
        pass

class Soundboard(TabbedPanelItem):
    pass

class SoundboardButton(Button):
    pass
PySoundboardApp().run()