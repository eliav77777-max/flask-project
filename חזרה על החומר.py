number=int(input('enter your num:'))
if number >0:
    print('the number is positive')
elif number<0:
    print('the number is negative')
else :
    print('the number is zero')

score=int(input('enter your score:'))
if score >=90:
    print('excellent')
elif score <90 and score >= 70:
    print('good')
elif score >69 and score <=50:
    print('pass')
else:
    print('fail')

for i in range (20):
    print ( i)
for i in range(51):
    if i %2==0:
        print (i)
num1=int(input('enter your num:'))
num2=int(input('enter your num:'))
num3=int(input('enter your num:'))
num4=int(input('enter your num:'))
num5=int(input('enter your num:'))
numbers=num1,num2,num3,num4,num5
print(sum(numbers))

num=int(input('enter your num:'))
while num!=2:
    print('dont the number')
    num=int(input('enter your num:'))
    if num==2:
        print('true number')
        break
print(num)


