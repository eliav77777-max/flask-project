try :
    result= 5/0
except ZeroDivisionError:
    print('cannot divide by zero')
with open('data.txt','a+') as file:
    file.write ('new data in my new file')

# initialize a counter variable
count=0

with open('text_data.txt','w') as file:
    file.write('i believe in my self to get the first job in devops ')

try:
    num= int(7)
except ValueError:
    print('value error occurred')
else:
    print('no error occurred')

def safe_divide (x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'cannot divide by zero'
print(safe_divide(10,0))
