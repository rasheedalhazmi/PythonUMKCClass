import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))