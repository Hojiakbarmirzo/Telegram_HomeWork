  
import requests
import json
from pprint import pprint
token='1686179341:AAG_HHrqlXOlgpHhiG-yP3H8iX5iZoj3bIM'
url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url)
data=r.json()
updates=data['result']


for update in updates:
    massage=update['message']
    user=massage['from']
    first_name=user.get('first_name','')
    last_name=user.get('last_name','')
    print(f'{first_name} {last_name}')