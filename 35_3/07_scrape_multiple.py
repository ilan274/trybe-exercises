import parsel
from six_scrape_exceptions import fetch_content
import json


def extract_quotes(text):
    selector = parsel.Selector(text)
    quotes = []
    for quote in selector.css("div.quote"):
        text = quote.css("span.text::text").get()
        author = quote.css("small.author::text").get()
        tags = quote.css("a.tag::text").getall()
        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes


def get_all_quotes():
    base_url = "https://quotes.toscrape.com/"
    next_page = "/"
    quotes = []
    while next_page:
        content = fetch_content(base_url + next_page)
        quotes.extend(extract_quotes(content))

        next_page = (
            parsel.Selector(content).css("li.next > a::attr(href)").get()
        )
    return quotes


print(get_all_quotes())


# print(extract_quotes(fetch_content("https://quotes.toscrape.com/")))
