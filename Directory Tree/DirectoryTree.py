import os.path
import os
from pathlib import Path
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Print

layout = [
            [gui.Input(key = "path", default_text= 'Enter you path here'), ],
            [gui.B("Generate the dir Tree"), ]
        ]

def display(path, level = 0):
    try :
        path = Path(path)
        k = os.listdir(path)
        for i in k:
            if os.path.isfile(os.path.join(path, i)):
                Print("  "*level, "--F--", i)
            elif os.path.isdir(os.path.join(path, i)):
                Print("  "*level, "+-D--", i)
                display(os.path.join(path, i), level = level + 1)
            else:
                Print(i)
    
    except:
        Print("Enter right path")

    return 

window = gui.Window("DirTree", layout, resizable = True)

while True :
    event, values = window.read()
    if event == gui.WIN_CLOSED :
        break
    elif event == "Generate the dir Tree":
        s = display(values["path"], level = 0)
window.close()