from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

header = {"User-Agent": UserAgent().random}

source = requests.get("https://www.imdb.com/find/?q=interstellar&ref_=nv_sr_sm", headers=header).text
soup = BeautifulSoup(source, 'lxml')

print(soup.find('h1').text)

soup = soup.find('div', class_='sc-17bafbdb-2 ffAEHI')

for list in soup.find_all('div', class_='ipc-metadata-list-summary-item__tc'):
    name = list.a.text
    year = list.find_all('ul')[0].text
    try:
        casts = list.find_all('ul')[1].text
    except:
        casts = "blank"

    print({
        "name": name,
        "year": year,
        "casts": casts,
    })
