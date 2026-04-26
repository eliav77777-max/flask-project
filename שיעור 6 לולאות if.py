# total=0
# for i in range(1,101):
#     if i % 3==0 and i % 5==0:
#         total+=i
#         print(total)

text='hello'
reversed_text=''
i= len(text) -1
while i>=0:
    reversed_text+=text[i]
    i-=1
    print(reversed_text)

list1=['itay','piho','ofer']
list2=['itay','piho','dba']
common=[]
for item in list1:
    if item in list2:
        common.append(item)
print(common)

my_list=['hello','eliav','hi', 'hi']
my_new_list=[]
for item in my_list:
    if item not in my_new_list:
        my_new_list.append(item)
        print(my_new_list)

sentence='i studying python im my home'
words=sentence.split()
count=0
for word in words:
    count+=1
print(count)


user_input=''
while user_input!='exit':
    user_input=input()
print(user_input)


password = '1234'
attempts = 3

while attempts > 0:
    user_pass = input('enter password: ')

    if user_pass == password:
        print('password match')
        break
    else:
        attempts -= 1
        print('password does not match, try again')

else:
    print('password does not match')


num=2
while num<=50:
    print(num)
    num+=2

total=0
num=-1
while num !=0:
    num=int(input('enter number: '))
    total+=num



