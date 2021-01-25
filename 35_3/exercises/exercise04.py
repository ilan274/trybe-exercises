import requests
from parsel import Selector
from bs4 import BeautifulSoup

URL_BASE = (
    "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
)
headers = {"User-agent": "Mozilla", "Accept": "text/html"}

response = requests.get(URL_BASE, headers=headers)
selector = Selector(text=response.text)
soup = BeautifulSoup(response.text, "lxml")
final = soup.find("div", {"class": "col-sm-6 product_main"}).find("h1").text
print(final)
