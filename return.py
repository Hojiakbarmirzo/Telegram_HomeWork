import requests
import json
from pprint import pprint

def sentMSG(indx,answer):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    payload={
        'chat_id':indx,
        'text':answer
    }
    r=requests.get(url,params=payload)

token='1696683157:AAH3NeNVQfFeIwBQtBCAokCOb2hp9_773SQ'
url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url)
data=r.json()
updates=data['result']

""" for update in updates:
    message=update['message']
    text=message['text']
    user=message['from']
    user_id=user['id']
    sentMSG(user_id,text)
    print(user_id) """
i=0
while True:
    update=updates[i]
    message=update['message']
    text=message['text']
    user=message['from']
    user_id=user['id']
    sentMSG(user_id,text)
    i+=1

