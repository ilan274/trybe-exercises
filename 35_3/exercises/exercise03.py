import requests
from parsel import Selector
from bs4 import BeautifulSoup

URL_BASE = "https://scrapethissite.com/pages/advanced/?gotcha=headers"
headers = {"User-agent": "Mozilla", "Accept": "text/html"}

response = requests.get(URL_BASE, headers=headers)
selector = Selector(text=response.text)
soup = BeautifulSoup(response.text, "lxml")
final = soup.find("div", {"class": "col-md-4 col-md-offset-4"}).text.strip()
print(final)
assert "bot detected" not in response.text
