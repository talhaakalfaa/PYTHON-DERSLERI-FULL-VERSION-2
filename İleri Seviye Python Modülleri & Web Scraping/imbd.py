import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0"
}

html = requests.get(url, headers=headers).content 
soup = BeautifulSoup(html, "html.parser")
list = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li", limit=10)

for item in list:
    filmadi = item.find("h3", {"class":"ipc-title__text"}).text
    puanbilgisi = item.find("span", {"class":"ipc-rating-star"}).text
    print(filmadi, puanbilgisi)
    

