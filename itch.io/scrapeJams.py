from typing import Text
import requests
from bs4 import BeautifulSoup

url = "https://itch.io/jams"

page = requests.get(url).text

soup = BeautifulSoup(page, "lxml")
#print(soup.prettify())

gamejam_widget = soup.findAll("div", attrs= {"class":"jam"})

with open(r"BeautifulSoup\itch.io\GameJamsThisWeek.txt", "w", encoding= "utf-8") as txtfile :
    txtfile.write("ITCH.IO Featured GameJams".center(80) + "\n\n")
    txtfile.write(("#"*80)+"\n\n")
    pass

with open(r"BeautifulSoup\itch.io\GameJamsThisWeek.txt", "a", encoding= "utf-8") as txtfile :

    for jam in gamejam_widget :

        jam_title = jam.find("div", attrs= {"class" : "primary_info"}).select("h3")[0].text
        txtfile.write(f"Jam Title : {jam_title}\n")
        #print(jam_title)

        jam_desc = jam.find("div", attrs = {"class" : "primary_info"}).select("p")[0].text
        txtfile.write(f"Game Jam description : {jam_desc}\n")
        #print(jam_desc)

        jam_host = jam.find("div", attrs = {"class": "hosted_by meta_row"}).text
        txtfile.write(f'{jam_host}\n')
        #print(jam_host)

        jam_status = jam.find("div", attrs = {"class": "timestmap meta_row"}).text
        txtfile.write(f'{jam_status}\n')
        #print(jam_status)

        jam_joins = jam.find("div", attrs = {"class" : "jam_stats"}).text
        txtfile.write(f'{jam_joins}\n')
        #print(jam_joins)

        jam_rank = "Ranked" if jam.find("div", attrs = {"class" : "jam_ranked"}) else "Not Ranked"
        txtfile.write(f'Jam is {jam_rank}\n')
        #print(jam_rank)

        jam_link = jam.find("div", attrs= {"class" : "primary_info"}).select("a")[0].get("href")
        txtfile.write(f"Jam link : https://itch.io{jam_link}\n")
        #print(jam_link)

        txtfile.write("\n"+("*"*80)+"\n")

        #break

print("completed")