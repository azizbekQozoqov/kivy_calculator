from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Events:
    def change_label_text_by_click(label: Label, text: str):
        label.text = text
    def add_input_value(input: TextInput, value: str, append=True, root=''):
        if append:
            if value.lower() == "del":
                if not input.text == "0" or len(input.text) <= 1:
                    input.text = input.text[::-1][1:][::-1]
                else:
                    input.text = '0'
                return

            elif value == "+/-":
                if input.text.startswith("-"):
                    input.text = input.text.replace("-", "")
                elif input.text == "0":
                    pass
                else:
                    input.text = f"-{input.text}"
                return

            if input.text == "0":
                input.text = ""
                input.text += value
            else:
                input.text += value

        else:
            if value == "=":
                try:
                    data = eval(input.text)
                    input.text = str(data)
                except:
                    root.popup().open()
                return


            input.text = ""
            if value == "":
                input.text = "0"
            else:
                input.text += value