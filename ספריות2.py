import requests
url='https://dog.ceo/api/breeds/list/all'
response=requests.get(url)
data=response.json()
breeds=data['message']
for breed in breeds:
    print(breed)

import requests
url='https://dog.ceo/api/breeds/image/random/3'
response2=requests.get(url)
data2=response2.json()
images=data2['message']
for image in images:
    print(image)


import requests
url3= "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My New Post",
    "body": "This is the content of my new post."
}

response3=requests.post(url3,json=payload)
data3=response3.json()

print('created post id:', data3['id'])
print('title:', data3['title'])
print('body:', data3['body'])

import requests
url4='https://api.restful-api.dev/objects'
payload1={
    'name':'sample object',
    'data': {
    'attribute1':'value1',
    'attribute2':'value2'
}
}
response4=requests.post(url4,json=payload1)
data4=response4.json()
print('created post id:', data4['id'])
print('name:', data4['name'])
print('data:', data4['data'])

import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

# בדיקת סטטוס קוד
if response.status_code == 200:
    data = response.json()
    print("Cat Fact:", data["fact"])
else:
    print("Request failed with status code:", response.status_code)
