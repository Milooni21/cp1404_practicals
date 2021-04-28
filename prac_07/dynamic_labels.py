from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class DynamicLabelApp(App):

    def build(self):
        box = BoxLayout(orientation = "vertical")
        label1 = Button(text="Bob Brown")
        label2 = Button(text="Car Cyan")
        label3 = Button(text="Oren Ochre")

        box.add_widget(label1)
        box.add_widget(label2)
        box.add_widget(label3)

        return box

if __name__ == '__main__':
    dynamic_label_app = DynamicLabelApp()
    dynamic_label_app.run()