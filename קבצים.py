print('hello') #איתי הדביל

file=open('data.txt.py','r')
print(file.read())
content=file.read(100)
print(content)
file.close()
file1=open('output.txt','w')
file1.write('hello world')
file1.close()
with open('output.txt','r') as file:
    content=file.read()
    print(content)
with open('output.txt','r') as file:
    first_line=file.readline()
    print(first_line)
with open('output.txt','w') as file:
    file.write('hello from python')
with open ('tasks.txt','w') as file:
    file.write('task 1\n')
    file.write('task 2\n')
    file.write('task 3\n')


