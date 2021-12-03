
#5.1 一个简单的示例

#5.2 条件测试

#5-1、5-2略

#5.3 if语句

#5-3

print('\n\t5-3\n')
alien_color = 'red'

if alien_color == 'green':   #简单的if语句
    print('You got five points.')

alien_color = 'green'
if alien_color == 'green':   #注意冒号
    print('You got five points.')

#5-4

print('\n\t5-4\n')
alien_color = 'red'

if alien_color == 'green':   #if-else语句
    print('You got five points.')
else:
    print('You got ten points.')

#5-5

print('\n\t5-5\n')

alien_color = 'red'

if alien_color == 'green':   #if-elif-else结构
    print('You got five points.')
elif alien_color == 'yelow' :
    print('You got ten points.')
else:
    print('You got fifteen points.')

#5-6

print('\n\t5-6\n')

age = 4

if age < 2:   #使用多个elif结构
    print('You are a boby.')
elif age >= 2 and age < 4 :
    print('You are learning walking.')
elif age >= 4 and age < 13:
    print('YOu are a child.')
elif age >= 13 and age < 20:
    print('YOu are a teenager.')
elif age >= 20 and age < 65:
    print('YOu are an adult.')
else:   #谨慎使用else语句
    print('You are the old.')

#5-7

print('\n\t5-7\n')
favour_fruits = ['apple','banana','watermelon']

if 'apple' in favour_fruits:   #测试多个条件
    print('You really like apples.')

if 'banana' in favour_fruits:   
    print('You really like bananas.')
    
if 'watermelon' in favour_fruits:
    print('You really like watermelons.')

#5.4 使用if语句处理列表

#5-8

user = ['admin','kai','keven','li','zhang']

for use in user:   #检查特殊元素是否在列表
    if use == 'admin':
        print('Hello ' + use.title() + ',would you like to see a status report?' )
    else:
        print('Hello ' + use.title() + ',thank you for logging in again.')

#5-9

print('\n\t5-9\n')

if user:   #若为空列表将会执行else
    print('This is not a empty list.')
else:
    print('We need to find some users!')

for num in range(1,6,1):
    del user[0]

if user:   
    print('This is not a empty list.')
else:
    print('We need to find some users!')

#5-10

print('\n\t5-10\n')

current_users = ['John','Sandy','Mike','Jake','Boke']
new_users = ['jake','tim','peter','mike','rama']
for new_user in new_users:
    if new_user.title() in current_users:
        print("'" + new_user.title() + "'" + " has been used.Please use another name.")
    else:
        print("Congratulations!You can use this name.")

#5-11

print('\n\t5-11\n')

list = [1,2,3,4,5,6,7,8,9]
for num in list:
    if  num == 1:
        print(num,str(num) + 'st',sep='  ')
    elif num == 2:
        print(num,str(num) + 'nd',sep='  ')
    elif num == 3:
        print(num,str(num) + 'rd',sep='  ')
    else:
        print(num,str(num) + 'th',sep='  ')

#5.5 设置if语句的格式

#5-12、5-13略