import PySimpleGUI as gui

Converter = {
            "USD" : 73.8,
            "Euro": 86.2,
            "AUD" : 52.51,
            "CAD" : 55.23,
            "CNY" : 10.82,
            "SGD" : 53.85,
}

layout = [
        [gui.Text("Enter INR currency"), gui.Input(key = "IND", size = (20, 1))],
        [gui.Text("Convert To: "), gui.Combo(list(Converter.keys()), default_value="USD", size = (6, 4), key = "C")],
        [gui.B("Convert"), gui.Exit()]
]

window  = gui.Window("Currency Converter", layout, size= (300, 120), resizable=True)

while True:

    event, values = window.read()

    if event in [gui.WIN_CLOSED, "Exit"]:
        break
    if event == "Convert":
        gui.popup(values["C"], float(values["IND"])/Converter[values["C"]])
    
window.close()