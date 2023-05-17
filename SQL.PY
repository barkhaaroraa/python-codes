from kivy.app import App

from kivy.uix.button import Button

class KivyButton(App):

    def build(self):

        return Button(text="Welcome to LikeGeeks!",,font_size='30', pos=(300,350), size_hint = (.25, .18))

KivyButton().run()

