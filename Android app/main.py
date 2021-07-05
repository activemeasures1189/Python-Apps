from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json

Builder.load_file('design.kv')

class LoginScreen (Screen):
    def sign_up(self):
        # SELF: self refers to the instace to LoginScreen class. MANAGER: manager is object of Screen class
        self.manager.current = 'signup_screen'
class SignupScreen (Screen):
    def add_user(self, uname, pword):
        file = open('users.json')
        users = json.load(file)
        print(users)
        print('hello git')

class RootWidget (ScreenManager):
    pass

class MainApp (App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()