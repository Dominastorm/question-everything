import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
Builder.load_string('''
<CameraClick>:
    fileloc:fileloc
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
    Button:
        text: 'Capture'
        font_size:20
        size_hint_y: None
        height: '48dp'
        background_normal:''
        background_color: (0.19,0.8,0.55,0.7)
        on_press: root.capture()
        
    TextInput:
        text:"Upload file -(path)"
        halign:'center'
        font_size:20
        size_hint_y: None
        height: '48dp'
        id:fileloc
        
    Button:
        text: "Import file"
        font_size:20
        size_hint_y: None
        height: '48dp'
        background_normal:''
        background_color: (1,0,0,1)
        on_press: root.btn()
    
    
''')
input_file=None
class CameraClick(BoxLayout):
    def capture(self):          #function call to capture the image
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")#to save the filename based on current time
        input_file = "IMG_{}.png".format(timestr)#storing the filelocation to main file variable
        camera.export_to_png("IMG_{}.png".format(timestr))
        print(input_file)

    def btn(self):  #function call to import the file when the user enters the address
        fileloc = ObjectProperty(None)
        print(self.fileloc.text)
        input_file=self.fileloc.text

class TestCamera(App):#final class call to run 

    def build(self):
        return CameraClick()



TestCamera().run()