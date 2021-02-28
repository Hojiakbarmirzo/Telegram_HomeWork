import requests
import json
from pprint import pprint
token='1686179341:AAG_HHrqlXOlgpHhiG-yP3H8iX5iZoj3bIM'
url=f'https://api.telegram.org/bot{token}/sendMessage'
""" payload={
    'chat_id': 1051394478,
    'text': 'Hi'
}
r=requests.get(url, params=payload)
print(r.url)
print(r.json())
#1051394478
 """
 r=requests.get(url)
 data=r.json()
 updates=data['result']
 update=updates[2]
 message=update['message']
 chat=message['chat']
 titel=chat['title']
 print(titel)