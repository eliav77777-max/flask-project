words=['apple','banana','mango','grape','apple','mango']
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
            freq[word]=1
print(freq)

dict1={1:'a',2:'b',3:'c'}
dict2={1:'a',2:'d',3:'e'}
commom={}
for key in dict1:
    if key in dict2 and dict1[key]==dict2[key]:
        commom[key]=dict1[key]
print(commom)


data={'a':10, 'b':'hi','c':5, 'd':2.5}
total=0
for value in data.values():
    if isinstance(value , int):
        total+=value
print(total)

sentence='hello world hello python'
words=sentence.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else :
        freq[word]=1
print(freq)


data={'a':10, 'b':'hi','c':5, 'd':2.5}
swapped={}
for key ,value in data.items():
    swapped[value]=key
print(swapped)

data={'a':10, 'b':2,'c':5}
sorted_keys=sorted(data,key=data.get)
print(sorted_keys)

dicts=[
    {'name': 'eliav','age': 29},
    {'name': 'itay','age': 20 },
    {'name': 'almog', 'age': 25}
]
sorted_dicts=sorted(dicts,key=lambda x: x['age'])
print(sorted_dicts)

