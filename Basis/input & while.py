
#7.1 函数input()的工作原理

#7-1

print('\n\t7-1\n')
print('What kind of car do you want to lend?')
answer = input('Let me see if I can find you a Subaru.')   #让用户输入

#7-2

print('\n\t7-2\n')
answer = int(input('How many people do you have lunch?'))   #注意数据类型，输入默认为字符串
if answer > 8:
    print('Sorry,we don not have suitable table.')
else:
    print('Welcome to our restaurant!')

#7-3略

#7.2 while循环简介

#7-4

print('\n\t7-4\n')
add = ''
while add != 'quit':   #简单的while循环，注意冒号
    add = input('Please tell us what food  you are need.If you do not need anythin,please tell us "quit".')
    if add == 'quit':
        break
    elif add != 'quit':
        print('We will add ' + add + '.')

#7-5、7-6、7-7略

#7.3 使用while循环来处理列表和字典

#7-8

print('\n\t7-8\n')

sandwich_orders = ['apple','banana','orange']
finished_sandwiches = []
while sandwich_orders:   #若为空列表将不会执行while循环
    for sandwich in sandwich_orders:   #可以不使用for循环来直接添加删除
        finished_sandwiches.append(sandwich)
        print('I made your '+ sandwich + ' sandwich.')
        break   #bread和continue语句作用于循环即while循环或for循环，不作用于if语句
    sandwich_orders.pop(0)   #不能在for循环中直接删除列表的元素

print('We had made these sandwiches:')
for sand in finished_sandwiches:
    print(sand.title())

#7-9略
#7-10

print('\n\t7-10\n')

places = {}
paper = True   #使用标识
while paper:   #标识为True则执行循环
    an = input('Can you join our paper?(yes or no)')
    if an == 'yes':
        name = input('What is your name?')
        place = input('If you could visit one place in the world,where would you go?')
        places[name] = place
        paper = False
    elif ans == 'no':
        paper = False
    else:
        print('Please answer the question with "yes" or "no".')

print(places)
