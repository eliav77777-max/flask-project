import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)
data = response.json()

print(data["fact"])

import requests

ratings = {}

for i in range(10):
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    data = response.json()

    if data["type"] == "single":
        joke = data["joke"]
    else:
        joke = data["setup"] + " " + data["delivery"]

    print(f"\nJoke {i+1}:")
    print(joke)

    rating = int(input("Rate this joke (1-5): "))
    ratings[joke] = rating

average = sum(ratings.values()) / len(ratings)
print("\nAverage rating:", average)