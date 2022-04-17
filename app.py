from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from colors import parse_hex
from events import Events

Builder.load_file("W.kv")
Config.set('graphics', 'resizable', False)
Window.size = (350, 500)

class WarnPopUp(Popup):
    pass

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        self.orientation = "vertical"
        self.parse_hex = parse_hex
        self.Events = Events
        self.popup = WarnPopUp

        super().__init__(**kwargs)




class KivyCalCulatorApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    KivyCalCulatorApp().run()