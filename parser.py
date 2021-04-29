import requests



URL = 'https://tabletki.ua/uk/search/?q='

# https://citrus.ua/search?query=xiaomi&page=2

res = requests.get(URL, params={
    'query': 'аспирин'
})

print(res.text)
