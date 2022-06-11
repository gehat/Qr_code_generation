from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime
from oblako import edit_oblako
KV = '''
MyBL: 
 orientation: 'vertical'
 size_hint: (0.95, 0.95)
 pos_hint: {'center_x': 0.5, 'center_y':0.5}
 Label:
  font_size: "30" 
  text: root.data_label
 TextInput:
  id: Inp1
  multiline: False
  padding_y: (5,5)
  size_hint: (1, 0.5)
  on_text: app.process()
 TextInput:
  id: Inp2
  multiline: False
  padding_y: (5,5)
  size_hint: (1, 0.5)
  on_text: app.process()
 TextInput:
  id: Inp3
  multiline: False
  padding_y: (5,5)
  size_hint: (1, 0.5)
  on_text: app.process()
 Button:
  text: "Сгенерировать"
  bold: True
  background_color: '#00FFCE'
  size_hint: (1,0.5)
  on_press: root.callback()
'''


class MyBL(BoxLayout):
    data_label = StringProperty('Генерация QR кода')

    def callback(self):
        print('Создание кода')
        # print(self.ids.Inp1.text,self.ids.Inp2.text,self.ids.Inp3.text,sep='\n')
        edit_oblako(self.ids.Inp1.text, self.ids.Inp2.text, self.ids.Inp3.text)
        with open('output.txt', 'a+', encoding="utf-8") as infile:
            infile.write(f'пользователь добавил информацию {str(datetime.today())[:19]} \n')
        self.ids.Inp1.text = ''
        self.ids.Inp2.text = ''
        self.ids.Inp3.text = ''


class MyApp(App):
    running = True

    def process(self):
        name = self.root.ids.Inp1.text
        author = self.root.ids.Inp2.text
        url = self.root.ids.Inp3.text

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()
