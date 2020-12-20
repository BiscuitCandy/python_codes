from bs4 import BeautifulSoup
import requests
import os.path
#import selenium

url = "https://dev.to/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title.text)

details = soup.select('div.crayons-story__indention')
with open(r'C:\Users\VIVEK VR\Documents\Python\BeautifulSoup\articles.txt', 'w') as f:
    for block in details :
        header = block.select('h2.crayons-story__title > a')[0].text.strip()
        link = block.select('h2.crayons-story__title > a')[0].get('href')
        f.write("dev.to"+link)
        f.write("\n")
print("done")
