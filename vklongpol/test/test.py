import requests
import random
import os
import  urlopen
import codecs
from PIL import Image
ra = str(random.randint(3,44444444))
parans={'access_token' : 'access_token',
            'group_id' : 'group_id',
            
            
            'v':'5.95'
          }

a= requests.get(url = 'https://api.vk.com/method/photos.getMessagesUploadServer?',params=parans)
res= a.json()
print(a.text)
upload_url=res['response']['upload_url'] 
print(upload_url)

files = { 'photo' : open('1.jpg', 'rb')}
b = requests.post(upload_url, files=files)
print(b.text)
resb =b.json()
photo = resb['photo']
print(photo)
server = resb['server']
print(server)
hashphoto = resb['hash']
print(hashphoto)
parans2={
    'access_token' : 'access_token',
    'photo':photo,
    'server':server,
    'hash':hashphoto,
    'v':5.59
}
c= requests.get(url = 'https://api.vk.com/method/photos.saveMessagesPhoto?',params=parans2)
print(c.text)
