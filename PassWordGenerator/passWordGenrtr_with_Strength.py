import random
import PySimpleGUI as gui

# define the gui layout
layout = [
            [gui.Text("Size", pad=(90, 20)), gui.Combo(list(range(8, 17)), default_value = 8, key = "size", size=(6, 10), pad = (10, 10))],
            [gui.Text("Strength", pad=(80, 0)), gui.Combo(["Weak", "Midcore", "Strong"], default_value = "Midcore", key = "strength", size= (10, 3))],
            [gui.Input(key="pass", size = (16, 3), default_text = "P@S$C0D3", pad = (150, 20))],
                        [gui.Button("Generate", focus = True, size=(10, 2), pad = (150, 10))]

] 


#Initialize the gui Window
window = gui.Window("PassWordGenerator", layout, size = (400, 250))

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

        #### Weak ---- only lower Aplhabet and numbers included
        if values["strength"] == "Weak" :
            password = "".join(random.sample("".join([small, numbers]),values["size"]))
        
        #### Mid Core ---- Capitals, lowers, numbers included
        elif values["strength"] == "Midcore" :
            password = "".join(random.sample("".join([small, capital, numbers]),values["size"]))
        
        #### Strong ---- All the characters can be used
        else :
            password = "".join(random.sample("".join([small, capital, numbers, symbols]),values["size"]))

        # Update the password on to the screen
        window["pass"].update(password)

    #closing the window
    if event == gui.WIN_CLOSED :
        break

window.close()