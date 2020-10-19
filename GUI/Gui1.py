import PySimpleGUI as gui

gui.theme("Dark Amber")

layout = [
            [gui.Text("Hi!, whats'up?",size = (20, 5), auto_size_text= True)],
            [gui.Quit()]
]

window = gui.Window("GUI", layout)

events, values = window.read()

window.close()