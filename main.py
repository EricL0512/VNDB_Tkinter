import requests

from tag import Tag

url = "https://api.vndb.org/kana/vn"
headers = {"Content-Type": "application/json"}
data = {
    "fields": "title, image.url, rating, tags.name, developers.name",
    "filters": ['and', ["search", "=", "Clannad"], ['rating', '>', '11'], ['developer', '=', ['search', '=', 'prototype']], ],
    "sort": "searchrank",
    "results": 10
}
response = requests.post(url, headers=headers, json=data)
result_json = response.json()
# Assuming the response contains a 'title' field
for i in result_json['results']:
    print(i)
for i in result_json['results']:
    print(i['title'])
    print(i['rating'])
    print('     ', end='')
    tags_amount = 0
    for j in i['tags']:
        tags_amount += 1
        print(j['name'], end=' ')
        if tags_amount > 10:
            break
    print()
    for j in i['developers']:
        print(j['name'], end=' ')
    print()