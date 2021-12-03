
#6.1 一个简单的字典

#6.2 使用字典

#6-1

print('\n\t6-1\n')
message = {'first_name':'Li','last_name':'Hua','age':'22','city':'HeFei'}   #创建字典，键值之间用冒号，键值对之间用逗号
print('Name: ',message['first_name'],message['last_name'])   #访问字典的值
print('Age: ',message['age'],'\nCity: ',message['city'])

#6-2略
#6-3

print('\n\t6-3\n')
dictionary = {}   #创建空字典

dictionary['print'] = '打印'   #添加键值对
dictionary['list'] = '列表'
dictionary['tuple'] = '元素'
dictionary['statement'] = '语气'
dictionary['function'] = '函数'
dictionary['method'] = '方法'

dictionary['tuple'] = '元组'   #修改字典键值对
del dictionary['statement']   #删除字典键值对
print(dictionary)

#6.3 遍历字典

#6-4

print('\n\t6-4\n')
for key,value in dictionary.items():   #使用方法遍历所有的键值对
    print(key,':',value)

#6-5

print('\n\t6-5\n')
rivers = {'nile':'egypt','yellowriver':'china','mississippi':'american'}

for river in rivers.keys():   #使用方法遍历所有的键
    print(river.title())

print('\n')

for country in rivers.values():   #使用方法遍历所有的值
    print(country.title())

#6-6

print('\n\t6-6\n')
favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python',  }
for peo in sorted(favorite_languages.keys()):   #按照字母顺序遍历字典所有的键
    print(peo.title() + ',thank you finish our paper! ' )

#6.4 嵌套

#6-7略
#6-8

print('\n\t6-8\n')
candy = {'name':'gao','kind':'cat'}
taidi = {'name':'qian','kind':'dog'}
timi = {'name':'zhai','kind':'rabbit'}

pets = [candy,taidi,timi]   #字典嵌套在列表中

for pet in pets:
    for top_1 in pet['name']:
        print(top_1)
    for top_2 in pet['kind']:
        print(top_2)

#6-9

print('\n\t6-9\n')
fav_places = {
    'fenng':['shanghai','dongbei','nanjing'],
    'caoz':['xinjiapo','hangzhou'],
    'stormzhang':['anhui','sanya','guangzhou']}   #列表嵌套在字典中

print(fav_places)

for place in fav_places['fenng']:   #访问字典键对应的值
    print(place)

#6-10略
#6-11

print('\n\t6-11\n')
cities = {
    'hangzhou':{'country':'China','population':'10000000'},
    'huashendun':{'country':'American','population':'8000000'},
    'london':{'country':'England','population':'5000000'}}   #字典嵌套在字典中

print('Cities','Country','population',sep='    ')

for ke,valu in cities.items():
    lists = []
    for val in valu.values():
        lists.append(val)
    print(ke,lists[0],lists[1],sep='    ')

for ke,val in cities.items():
    print(ke,val['country'],val['population'],sep='    ')   #这两行可以代替上五行

#6-12略