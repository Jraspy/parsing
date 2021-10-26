# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json
url = 'http://api.weatherbit.io/v2.0/current'
key = '30c59a5df2c54e6a8e187f4cbfbd2dfb'
lat = '55.558741'
lon = '37.378847'

req = requests.get(f'{url}?lat={lat}&lon={lon}&key={key}')
data = json.loads(req.text)
print(data)

with open('weatherbit.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)