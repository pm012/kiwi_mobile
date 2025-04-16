from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window

from logic.calculator import Calculator
from logic.state_factory import StateFactory

Window.size = (300, 400)

class KivyCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)       
        self.calc = Calculator()

        self.display = TextInput(
            font_size=40, size_hint_y=0.2,
            readonly=True, halign='right',
            multiline=False, text='0'
        )
        self.add_widget(self.display)

        keys = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['C', '0', '=', '/']
        ]

        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in keys:
            for key in row:
                btn = Button(text=key, font_size=30)
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)
        self.add_widget(grid)

    def on_button_press(self, instance):
        key = instance.text
        self.calc.press(key)
        self.display.text = self.calc.show()

class CalculatorApp(App):
    def build(self):
        return KivyCalculator()

if __name__ == '__main__':
    CalculatorApp().run()
