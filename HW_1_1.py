# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import json

import requests
user = 'JRASPY'
req = requests.get(f'https://api.github.com/users/{user}/repos')
data = json.loads(req.text)
for item in data:
    print(item['name'])

with open('github_repos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)