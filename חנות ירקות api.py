import requests
url='https://official-joke-api.appspot.com/jokes/random'
while True :
    response = requests.get(url)
    joke=response.json()
    if 'banana' in joke['setup'] or 'banana' in joke ['punchline']:
        print (joke['setup'])
        print (joke['punchline'])
        break


