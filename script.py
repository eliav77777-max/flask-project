import requests
url = "https://official-joke-api.appspot.com/jokes/random"
while True:
  response=requests.get(url)
  joke=response.json()
  full_joke = joke["setup"] + " " + joke["punchline"]
  if "banana" in full_joke.lower():
      print("joke with banana!\n")
      print(full_joke)
      break