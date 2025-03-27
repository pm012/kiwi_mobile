from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (300, 500)

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        #Build out the app
        self.result = TextInput(
            font_size=45,
            size_hint_y=0.2,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=[0.2, 0.2, 0.2, 1],
            foreground_color =[1,1,1,1],
            text = "0"
        )
        self.add_widget(self.result)

    


        #Create the buttons
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]

        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for item in row:
                button = Button(
                    text = item,
                    font_size=32,
                    background_color=self.set_button_color(item),
                    on_press = self.button_click
                )
                grid.add_widget(button)
        self.add_widget(grid)
    
    def set_button_color(self, label):
        if label in {'C', '+/-', '%'}:
            return [0.6,0.6,0.6,1]
        elif label in {"/", "*", "-", "+", "="}:
            return [0.988, 0.631, 0.012, 1]
        return [0.3,0.3,0.3,1]




    def button_click(self, instance):
        text = instance.text        

        if text == "C":
            self.result.text ="0"
        elif text == "=":
            self.calculate()
        elif text == "+/-":
            self.toggle_neg()
        elif text == "%":
            self.convert_percent()
        else:
            if self.result.text == "0" and text not in {"+", "-", "*", "/", ".", "+/-"}:
                self.result.text = text  # Replace "0" with new number
            else:
                self.result.text += text  # Append normally
    
    
     
    def calculate(self):  
        try:            
            self.result.text = str(eval(self.result.text))
        except (SyntaxError, ValueError):
            self.result.text = "ERROR"

    def toggle_neg(self):
        if self.result.text and self.result.text!="0":
            self.result.text = self.result.text[1:] if self.result.text[0] == "-" else "-" + self.result.text

    def convert_percent(self):
        try:
            self.result.text = str(float(self.result.text)/100)
        except ValueError:
            self.result.text = "ERROR"

            


class CalculatorApp(App):
    def build(self):
        return Calculator()
    
if __name__ == "__main__":
    CalculatorApp().run()
    

