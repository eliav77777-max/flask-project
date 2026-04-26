import requests
url='https://restcountries.com/v3.1/all?fields=name,population,region'
response=requests.get(url)
data=response.json()
print(len(data))
count=0
for country in data :
    print(country['name']['common'])
    count+=1
    if count == 10:
        break

for country in data :
    if country ['region']=='Europe' :
        print(country['name']['common'])
user_country=input("Enter your country")
for country in data :
    if country ['name']['common']==user_country :
        print( 'country:',country['name']['common'])
        print('population:',country['population'])
max_country = data[0]
for country in data:
    if (country['population'] >
    max_country['population']):
        max_country = country

print("Most populated country is:", max_country['name']['common'])
print("Population:", max_country['population'])

