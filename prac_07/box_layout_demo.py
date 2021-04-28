from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class BoxLayoutDemo(App):
    greeting_message = StringProperty()
    name_input = StringProperty()

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.name_input = self.root.ids.input_name.text
        self.greeting_message = "Hello " + self.name_input

    def handle_clear(self):
        self.greeting_message = ""
        self.name_input = ""


if __name__ == '__main__':
    box_layout_demo = BoxLayoutDemo()
    box_layout_demo.run()
