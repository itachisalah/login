from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size=(350,600)


class Facebook(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Brown"
        return Builder.load_file('main.kv')

    def logger(self):
        self.root.ids.welcome_label.text= f'Welcome {self.root.ids.user.text}?'

    def clear(self):
        self.root.ids.welcome_label.text="WELCOME"
        self.root.ids.user.text=""
        self.root.ids.password.text=""


Facebook().run()