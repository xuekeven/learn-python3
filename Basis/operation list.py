
#4.1 遍历整个列表

#4.2 避免缩进错误

#4-1

pizzas = ['肉夹馍','手抓饼','鸡蛋灌饼','煎饼果子']

print('\n\t4-1\n')
for pizza in pizzas:   #for循环
    print('我喜欢吃' + str(pizza))

print('我太吃喜欢面食了！')

#4-2

animals = ['dog','cat','rabbit']

print('\n\t4-2\n')
for animal in animals:   #注意冒号
    print('A ' + str(animal) + ' tastes delicious.')   #注意缩进

#4.3 创建数值列表

#4-3

print('\n\t4-3\n')
for xunhuan in range(1,21,1):   #随机生成数字的函数
    print(xunhuan)

#4-4

print('\n\t4-4\n')
numbers = []   #创建空列表

for number in range(1,101,1):
    numbers.append(number)   #创建数字列表

for num in numbers:
    print(num)

#4-5
print('\n\t4-5\n')
numbers = []

for number in range(1,1000001,1):
    numbers.append(number)   

print(min(numbers))   #找出数字列表最小值的函数
print(max(numbers))   #找出数字列表最大值的函数
print(sum(numbers))   #求出数字列表之和的函数

#4-6、4-7略
#4-8

print('\n\t4-8\n')
lifang = []
for num in range(1,11):
    lifang.append(num**3)
    
for num in lifang:
    print(num)

#4-9

print('\n\t4-9\n')
cube = [value**3 for value in range(1,11,1)]   #列表解析
print(cube)

#4.4 使用列表的一部分

#4-10

print('\n\t4-10\n')
print('The first three items in the list are:',cube[:3],sep='\n')   #使用切片遍历最前三元素
print('Three items from the middle of the list are:',cube[4:7],sep='\n')   #使用切片遍历中间三元素
print('The last three items in the list are:',cube[-3:],sep='\n')   #使用切片遍历最后三元素
 
#4-11

print('\n\t4-11\n')
friend_pizzas = pizzas[:]   #使用切片复制列表创建副本
pizzas.append('阜阳卷馍')
friend_pizzas.append('驴肉卷饼')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12略

#4.5 元组

#4-13

restaurant = ('猪肉','牛肉','羊肉','鸡肉','兔肉')   #创建元组
print('\n\t4-13\n')
for food in restaurant:   #遍历元组的所有值
    print(food)

restaurant = ('驴肉','狗肉','羊肉','鸡肉','兔肉')   #元组不能修改，只能重新赋值

print('\n改后的元组：\n')
for food in restaurant:   
    print(food)

#4.6 设置代码格式

#4-14、4-15略