import requests
import json

# Dla Niemiec
country_cases = 'Germany'
url = "https://covid-api.mmediagroup.fr/v1/cases?country={}".format(country_cases)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)

expected = ['country', 'capital_city', 'continent', 'population', 'confirmed', 'recovered', 'deaths']
current = []
# Wartosci
for key, value in a.items():
    for k, v in value.items():
        if k == 'country':
            country = v
        if k == 'population':
            population = v
        if k == 'capital_city':
            capital_city = v
        if k == 'deaths':
            deaths = v

assert country_cases == country
assert country_cases == 'Germany'
# Klucze
for key, value in a.items():
    for k, v in value.items():
        if k in expected:
            current.append(k)
assert expected == current
# Odpowiedzi
assert response.status_code == 200
assert response.status_code == 201
assert response.status_code == 202
# Zle zapytanie
url = "https://covid-api.mmediagroup.fr/v1/a?country={}".format(country_cases)
response = requests.request("GET", url)
assert response.status_code == 403

# Dla Francji
country_cases2 = 'France'
url = "https://covid-api.mmediagroup.fr/v1/cases?country={}".format(country_cases2)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
i = json.loads(response.text)

expected = ['country', 'capital_city', 'confirmed', 'recovered', 'deaths', 'sq_km_area']
current = []
# Wartosci
for key, value in i.items():
    for k, v in value.items():
        if k == 'country':
            country = v
        if k == 'confirmed':
            confirmed = v
        if k == 'capital_city':
            capital_city = v
        if k == 'recovered':
            recovered = v
        if k == 'sq_km_area':
            sq_km_area = v

assert country_cases2 == country
assert country_cases2 == 'France'
# Zle zapytanie
url = "https://covid-api.mmediagroup.fr/v1/a?country={}".format(country_cases2)
response = requests.request("POST", url)
assert response.status_code == 401
