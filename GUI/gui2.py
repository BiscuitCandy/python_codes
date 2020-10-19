import PySimpleGUI as gui
x = ""
layout =[
        #layout
]

window = gui.Window("Title", layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == gui.WIN_CLOSED:
        break
    elif event == "Event_name":
        ##Body
        pass