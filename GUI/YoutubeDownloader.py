from pytube import YouTube
import PySimpleGUI as gui
import os.path

gui.theme("Material1")

layout = [
          [gui.Text("Enter the Video URL")],
          [gui.Input(key = "URL")],
          [gui.Input(key = "Path"), gui.FolderBrowse(target="Path", initial_folder=os.path.abspath(r"\Downloads"))],
          [gui.Text("", key = "Rlt", size=(20,1))],
          [gui.B("Download"), gui.Exit()]
        ]

window = gui.Window("YouTube Downloader", layout,size=(400, 180), resizable=True)

while True:
    event, values = window.read()
    if event in [gui.WIN_CLOSED, "Exit"]:
        break
    if event == "Download": 
        try:
            yt = YouTube(values["URL"])
            a = yt.streams.filter(progressive =  True)[-1]
            Details = "Title: {0} \n Views: {1} \n Length: {2}".format(
                                        yt.title, yt.views, yt.length)
            window.FindElement("Rlt").Update(Details)
            #gui.Print("Get to the try section")
            if os.path.isdir(values["Path"]):
                if a:
                     a.download(values["Path"])
                else:
                    a = yt.streams[-1]
                    a.dowmload(values["Path"])
                #gui.Print("got It!")
            else:
                window.FindElement("Rlt").update("Give valid Directory")
                gui.popup("Please Specify a valid directory to download")
        except:
            gui.popup("There Seems to be a Problem")
        
window.close()