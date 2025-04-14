from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label  # Still needed if using Label in kv
from kivy.lang import Builder

Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '665')

class MyApp(App):
    def build(self):
        self.icon = "pngegg.png"
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    MyApp().run()
