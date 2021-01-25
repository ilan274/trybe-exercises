import requests


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text


# print("Correto: ", fetch_content("https://quotes.toscrape.com/"))
# print("Vazio: ", fetch_content("https://httpbin.org/status/404"))
# print("Demora mais de 1 segundo pra responder: ", fetch_content("https://httpbin.org/delay/3"))
# print("Demora menos de 1 segundo pra responder: ", fetch_content("https://httpbin.org/get"))
