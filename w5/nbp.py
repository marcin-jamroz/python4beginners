import requests


# ogólnie to rzuca sporo wyjątków, więc lepiej obsługiwać
url = "http://api.nbp.pl/api/exchangerates/tables/A/"
r = requests.get(url=url)
print(r)

# print(dir(r))

from pprint import pprint
# order = ('headers', 'raw', 'status_code', 'ok', 'request', 'url', 'content', 'text', 'json')
# for attr in order:
#     print(attr)
#     pprint(getattr(r, attr))
#     print(80 * '-')
# print('json')
# pprint(r.json())

for x in r.json():
    print("type(x):", type(x))
    pprint(x)
    print(80*"-")
