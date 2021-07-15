# 

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreen (Screen):
    def sign_up(self):
        # SELF: self refers to the instace to LoginScreen class. MANAGER: manager is object of Screen class
        self.manager.current = 'signup_screen'
    def login(self, uname, pword):
        file = open('users.json')
        users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Incorrect Username or Password!"

class SignupScreen (Screen):
    def add_user(self, uname, pword):
        file = open('users.json')
        users = json.load(file)
        users[uname] ={'username': uname, 'password':pword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        file = open('users.json', 'w')
        json.dump(users,file)
        self.manager.current = "signup_screen_success"
class SignupScreenSuccess (Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
class LoginScreenSuccess (Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    def get_quote(self, mood):
        self.ids.mood.text = mood
        
        if mood.lower() == 'sad':
            data = open('sad.txt', 'r', encoding='utf8')
            file = data.readlines()
            self.ids.quote.text = random.choice(file)
        elif mood.lower() == 'happy':
            data = open('happy.txt', 'r', encoding='utf8')
            file = data.readlines()
            self.ids.quote.text = random.choice(file)
        elif mood.lower() == 'unloved':
            data = open('unloved.txt', 'r', encoding='utf8')
            file = data.readlines()
            self.ids.quote.text = random.choice(file)
        else:
            self.ids.quote.text = 'Invalid Input. Try words such as Happy, Sad, Unloved..'   
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

 

    

class RootWidget (ScreenManager):
    pass

class MainApp (App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()