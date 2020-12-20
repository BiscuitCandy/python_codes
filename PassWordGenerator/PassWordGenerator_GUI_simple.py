import random
import PySimpleGUI as gui

# define the gui layout
layout = [
            [gui.Text("Size"), gui.Combo(list(range(8, 17)), default_value = 8, key = "size")],
            [gui.Input(key="pass", size = (16, 1), default_text = "P@S$C0D3")],
                        [gui.Button("Generate", focus = True)]

] 


#Initialize the gui Window
window = gui.Window("PassWordGenerator", layout, size = (200, 100))

# Requirements of the password
small = 'abcdefghijklmnopqrstuvwxyz'
capital = small.upper()
numbers = '1234567890'
symbols = '_!@#$%^&*+-><'

# now the gui implementation begins
while True:
    event, values = window.read()

    if event == "Generate" :
        #password generator
        # Create a random password from above data
        password = "".join(random.sample("".join([small, capital, numbers, symbols]),values["size"]))
        window["pass"].update(password)
    if event == gui.WIN_CLOSED :
        break

window.close()