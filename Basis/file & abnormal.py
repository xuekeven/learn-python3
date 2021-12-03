
#10.1 从文件中读取数据

#10-1

print('\n\t10-1\n')
file_path = 'D:/Learn/Python/Basis/learning_python.txt'   #使用绝对路径打开文件，路径前加r表示rawstring（原生字符串）

with open(file_path) as file_object:   #函数默认为只读模式('r')
    contents = file_object.read()   #方法读取整个文件并且保存在变量中
    print(contents)   #read()阅读文件末尾时会返回空字符串显示为空行

with open(file_path) as file_object:   
    for line in file_object:   #逐行读取文件
        print(line)   #文件每行末尾都有换行符


with open(file_path) as file_object:   
    lines = file_object.readlines()   #包含文件各行内容的列表
for line in lines:
    print(line)

#10-2

print('\n\t10-2\n')
file_path = 'D:/Learn/Python/Basic/learning_python.txt'   
with open(file_path) as file_object:   
    contents = file_object.read()   
    print(contents)   

    li = contents.replace('python','d')   #替换
    print(li)

#10.2 写入文件

#10-3
'''
提示用户输入其名字
'''
print('\n\t10-3\n')
guests = 'D:/Learn/Python/Basic/guests.txt'
def input_name():

    name = input('Please write your name.')

    with open(guests,'w') as files:   #打开文件为写入模式，将覆盖原文件内容，文件不存在将会创建
        files.write('User:')   #写入文件
        files.write(name + '\n')   #写入多行

input_name()

#10-4略
#10-5

print('\n\t10-5\n')
lover = 'D:/Learn/Python/Basic/lover.txt'

ai = True
while ai:
    reason = input('Can you tell us why you like coding?')
    if reason != 'quit':
        with open(lover,'a') as files:   #打开文件为附加模式，会保留原内容写入，('r+')能够读取和写入
            files.write('The reason:\n')
            files.write(reason + '\n')
    else:
        ai = False

with open(lover) as file_o:   
    lines = file_o.readlines()   
for line in lines:
    print(line)

#10.3 异常

#10-6 & 10-7

'''
提示用户提供数值输入时，常出现的一个问题是，用户提供的是
文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
的程序进行测试：先输入两个数字，再输入一些文本而不是数字。编写的代码放在
一个 while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
'''
while True:
    numbers = []
    print('Please give us two numbers.')
    num1 = input('Number1:')
    num2 = input('Number2:')
    try:
        number1 = int(num1) 
        number2 = int(num2)
        number = number1 + number2
        break
    except ValueError:   #告诉python遇到ValueError应该怎么办
        print('Please number!')
        continue

numbers.append(number)
print(numbers)

#10-8 & 10-9
'''
创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的名字，
在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容
打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获
FileNotFound错误，并打印一条友好的消息。将其中一个文件移到另一个地方，并确认
except代码块中的代码将正确地执行。修改except代码块，让程序在文件不存在时一言不发。
'''
print('10-8 & 10-9')

file1 = 'D:/Learn/Python/Basic/cats.txt'
file2 = 'D:/Learn/Python/Basic/dogs.txt'
try:
    with open(file1) as f1:
        line1 = f1.readlines()
        print('Cats:')
        for line in f1:
            print(line)

    with open(file2) as f2:
        line2 = f2.readlines()
        print('Dogs:')
        for line in line2:
            print(line)
 
except FileNotFoundError:
    pass   #告诉python什么都不要做
else:   #代码没有异常后运行
    print("That's all names.")

#10-10略

#10.4 存储数据

#10-11 & 10-12
'''
编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It’s _____.”。
两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字
并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
'''
print('10-11 & 10-12')

import json
file2 = 'D:/Learn/Python/Basic/numbers.json'
try:
    with open(file2) as fl:
        numbers = json.load(fl)   #读取json数据文件
except FileNotFoundError:
    num = int(input('Which number is your favourite?'))
    with open(file2,'w') as f:

        json.dump(num,f)   #存储数据至json文件中
        print('We will remember your favourite number:' + str(num) + '.')
else:
    print('I know your favorite number! It’s ' + str(numbers) +' .')

#10-13略