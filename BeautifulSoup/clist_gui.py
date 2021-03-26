import PySimpleGUI as gui
import requests 
import json

from bs4 import BeautifulSoup

url = "https://clist.by"

webpage = requests.get(url, allow_redirects = True).text

soup = BeautifulSoup(webpage, "lxml")

total_items = 20

contest_list = [json.loads(i.get("data-ace")) for i in soup.find_all("a", attrs = {"class" : "data-ace"})[:total_items] ]

gui.theme("Dark Amber")

layout = [
    [gui.B("Get Contest Details")]
        ]

contest = 0

window = gui.Window("CLIST", layout, size = (200, 100), margins = (30, 30), auto_size_buttons = True)

while True:
    event, values = window.read()

    if event in [gui.WIN_CLOSED, "Close"]:
        break

    if event == "Get Contest Details" :
        window.close()
        layout = [
            [gui.Text(contest_list[contest]["title"], key = "title", size = (50, 1))],
            [gui.Text(contest_list[contest]["desc"], key = "link", size = (50, 1))],
            [gui.Text(contest_list[contest]["time"]["start"], key = "startTime", size = (32, 1))],
            [gui.Text(contest_list[contest]["time"]["end"], key = "endTime", size = (32, 1))],
            [gui.Text("All the TimeZone are in UTC-(+0:00)")],
            [gui.B("Next")]
        ]
        window = gui.Window(contest_list[contest]["title"], layout, size = (500, 200), resizable = True)

    if event == "Next" :
        contest += 1
        if contest == total_items :
            window.close()
            layout = [[gui.Text("No More Results")], 
                    [gui.B("Close")]
            ]
            window = gui.Window("End", layout, size = (200, 500))
        else :
            window["title"].update(contest_list[contest]["title"])
            window["link"].update(contest_list[contest]["desc"])
            window["startTime"].update(contest_list[contest]["time"]["start"])
            window["endTime"].update(contest_list[contest]["time"]["end"])
