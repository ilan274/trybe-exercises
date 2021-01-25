import requests

URL_BASE = "https://api.github.com/users"
response = requests.get(URL_BASE)
json_response = response.json()

for user in json_response:
    login = user['login']
    url = user['url']
    print(login, url)
