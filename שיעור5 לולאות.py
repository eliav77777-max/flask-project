num=int(input('Enter a number: '))
if num>0:
    print('is positive')
elif num < 0 :
        print('is negative')
else:
        print('is zero')

year=int(input('Enter a year: '))
if year % 400 == 0:
    print('leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('leap year')
else :
    print('not a leap year')


num=int(input('Enter a number: '))
if num % 2==0:
    print('even number')
else:
    print('odd number')

a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=int(input('Enter another number: '))
print('the larget number is-', max(a,b,c))



text= input('Enter a word: ')
if text==text[::-1]:
    print('palindrome')
else:
    print('not a palindrome')

percent=int(input('enter percentage: '))
if percent >=90 :
    print('grade A')
elif percent >=80 :
    print('grade B')
elif percent >=70 :
    print('grade C')
elif percent >=60 :
    print('grade D')
else:
    print('fail')

year=int(input('Enter a year: '))
if year % 100==0:
    print('century year')
else:
    print('not a century year')

import math
num= int(input('Enter a number: '))
if math.isqrt(num) **2==num:
    print('the number is a perfect square')
else:
    print('not a perfect square')











