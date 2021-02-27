import PDFReader as pr
import TextRecognition as tr

import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
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

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass


input_file=None
class CameraClick(BoxLayout):
    def capture(self):          #function call to capture the image
        camera = self.ids['camera']
        # timestr = time.strftime("%Y%m%d_%H%M%S")#to save the filename based on current time
        input_file = "image.png"#storing the filelocation to main file variable
        camera.export_to_png("image.png")
        f = open("text.txt", "w")
        f.write(tr.ImageReader(input_file))
        f.close()
        TestCamera().stop()

    def btn(self):  #function call to import the file when the user enters the address
        fileloc = ObjectProperty(None)
        location = self.fileloc.text
        f = open("text.txt", "w")
        if location[-3:] in ("png", "peg", "jpg"):
            f.write(tr.ImageReader(location))
        elif location[-3:] == "pdf":
            f.write(pr.ReadPDF(location))
            pass
        elif location[-3:] == "txt":
            f.write(open(location, "r").read())
        else:
            pass

        f.close()
        input_file=self.fileloc.text
        TestCamera().stop()

class TestCamera(App):#final class call to run

    def build(self):
        return CameraClick()



TestCamera().run()