
#8.1 定义函数

#8-1

print('\n\t8-1\n')
def display_message():   #定义简单的函数，注意冒号
    print('You learn Function in this passage.')

display_message()   #注意运行函数

#8-2

print('\n\t8-2\n')
def favorite_book(title):   #定义形参无需引号，类似于“变量”
    print('One of my favorite books is ' + title +'.')   #定义形参后函数内最好没有其它变量

favorite_book('Alice')   #传递实参需要确定实参的数据类型

#8.2 传递实参

#8-3

print('\n\t8-3\n')
def make_shirt(size,sentence = 'I love python!'):   #可定于多个形参,也可以给形参默认值，给形参指定默认值时，等号两边不要有空格
    print('Your shirt sizw is ' + size.title() + '.')
    print('"' + sentence.title() + '"' + ' will printed on your shirt.' )   #多个单词组成的字符串使用title()函数时每个单词都会首字母大写

make_shirt('m','work hard!')   #使用位置实参调用，注意位置
make_shirt(sentence = 'i love you.',size = 'l')   #使用关键字实参调用
make_shirt('xl')   #不赋予实参时使用默认值

#8-4略
#8-5

print('\n\t8-5\n')
def describe_city(city,country = 'China'):
    print(city.title() + ' is in ' + country.title() + '.')

describe_city('beijing')
describe_city('nanjing')
describe_city('londun','england')

#8.3 返回值

#8-6

print('\n\t8-6\n')
def city_country(city,country):
    leixing = '"' + city.title() + ',' + country.title() + '"'
    return leixing   #函数返回值

shu = print(city_country('hangzhou','china'))

#8-7

print('\n\t8-7\n')
music = {}
def make_album(musicer,name,number = ''):   #把形参变为可选的
    music[musicer] = name
    if number:   #若传递number形参则执行此if语句
        music['number'] = number   #注意字典添加键值的方法
    return music   #返回字典

make_album('uyjhgf','vdf')
make_album('wqdesf','dgdr')
make_album('rgefv','tynbg',3)
 
print(music)

#8-8略

#8.4 传递列表

#8-9

print('\n\t8-9\n')
magician = ['cds','fsaf','hybr']
def show_magicians(magic):
    for mag in magic:
        print(mag.title())
    
show_magicians(magician)   #传递列表

#8-10 & 8-11

print('\n\t8-10 & 8-11\n')
magicians = []

def make_great(magic,magics):
    while magic:   #定义形参后函数内应该只有形参
        mag = magic.pop()
        mag = 'the Great ' + mag
        magics.append(mag)

make_great(magician[:],magicians)   #使用切片法传递列表的副本可以保留原列表
show_magicians(magicians)
show_magicians(magician)

#8.5 传递任意数量的实参

#8-12
'''
编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数
只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
调用这个函数三次，每次都提供不同数量的实参。
'''
print('\n\t8-12\n')
def order(*vegs):   #设置传递任意数量的参数（这样会生成一个空元组）
    print('Please tell us what you want to eat.')
    print(vegs)

order('eggs','apples')

#8-13略
#8-14
'''
编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受
制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息以及
两个名称—值对，如颜色和选装配件。
'''
print('\n\t8-14\n')

def cars(maker,model,**other):  #设置传递任意数量的参数（这样会生成一个空字典）
    car = {}
    car['maker'] = maker
    car['model'] = model
    for key,value in other.items():
        car[key] = value
    return car

print(cars('比亚迪','电动汽车',color = 'afd'))

#8.6 导入函数

import pizza   #导入整个模块
pizza.make_pizza(16,'pepperoni')

import pizza as pz   #导入整个模块并给模块指定别名
pz.make_pizza(16,'pepperoni')

from pizza import make_pizza   #从模块导入函数
make_pizza(16,'pepperoni')

from pizza import make_pizza as mp   #从模块导入函数，并给函数指定别名
mp(16,'pepperoni')

from pizza import *   #从模块导入所有函数
make_pizza(16,'pepperoni')

#8.7 函数编写指南

#8-15、8-16、8-17略