from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder

KV = """
 MDScreen:
        
     MDRaisedButton:
        text:"clique aqui"
        pos_hint:{'center_x':0.5, 'center_y':0.5}
"""
class BarbeariaApp(MDApp):

    def build(self):
        return Builder.load_string(KV)
    

    
BarbeariaApp().run()