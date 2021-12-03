
#3.1 列表是什么

#3-1

names = ['xue','wang','zhang']   #创建列表
print('\n\t3-1\n\n' + names[0] + '\n' + names[1] + '\n' + names[2])   #访问列表

#3-2

dazhaohu = 'Hello,'
print('\n\t3-2\n\n' + dazhaohu + names[0].title() + '!')
print(dazhaohu + names[1].title() + '!')
print(dazhaohu + names[2].title() + '!')

#3-3

vehicles = ['car','bus','train','metro','bicycle','motorcycle']

print('')

#3.2 修改、添加和删除元素

#3-4

invition = ['lao ye','my wife','my parents']

print('\n\t3-4\n')
print('Dear ' + invition[0].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[1].title()+ ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[2].title() + ',We will have a party tonight and hope you can come.')

#3-5

print('\n\t3-5\n\n' + 'Sorry, ' + invition[0].title() + " can't come.")

invition[0] = 'My sister'   #修改元素
print('Dear ' + invition[0].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[1].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[2].title() + ',We will have a party tonight and hope you can come.')

#3-6

invition.insert(0,'zi cong')   #添加元素方法一
invition.insert(2,'heng yu')
invition.append('zhai kai')   #添加元素方法二

print('\n\t3-6\n')
print('Dear ' + invition[0].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[1].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[2].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[3].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[4].title() + ',We will have a party tonight and hope you can come.')
print('Dear ' + invition[5].title() + ',We will have a party tonight and hope you can come.')


#3-7

print('\n\t3-7\n' + 'Sorry,there just two seats can be used.')
print(invition)

go_1 = invition.pop()   #删除元素的方法一，还使用被删除的元素
print('Sorry,' + go_1 + ',Let us play next time.')

go_2 = invition.pop(3)   #删除元素的方法二，还使用被删除的元素
print('Sorry,' + go_2 + ',Let us play next time.')

go_3 = 'heng yu'
invition.remove(go_3)   #删除元素的方法三，还使用被删除的元素
print('Sorry,' + go_3 + ',Let us play next time.')

go_4 = invition.pop()
print('Sorry,' + go_4 + ',Let us play next time.')

print('Dear ' + invition[0].title() + ',remember come here.')
print('Dear ' + invition[1].title() + ',remember come here.')

del invition[0]   #删除元素的语句，不使用被删除的元素
del invition[0]
print(invition)

#3.3 组织列表

#3-8

places = ['秦皇岛','南澳岛','北海','南宁','兰州']

print('\n\t3-8\n\n' + '原始列表：places=' ,places,sep='')   #打印多个值用，值与值之间用逗号隔开；sep=''表示打印出来的多个值之间不隔开

print('\n使用sorted()函数对列表顺序排序：',sorted(places))   #对列表临时顺序排序的函数
print('\n使用sorted()函数顺序排序后的列表：',places)

print('\n使用sorted()函数对列表倒序排序：',sorted(places,reverse=True))   #对列表临时倒序排序的函数
print('\n使用sorted()函数倒序排序后的列表：',places)

places.reverse()
print('\n使用reverse()方法反转列表：',places)   #对列表永久反转的方法，不是按照字母顺序相反的顺序排序列表

places.reverse()
print('\n再次使用reverse()方法反转列表：',places)

places.sort()
print('\n使用sort()方法对列表顺序排序：',places)   #对列表永久顺序排序的方法

places.sort(reverse=True)
print('\n使用sort()方法对列表倒序排序：',places)   #对列表永久倒序排序的方法

#3-9

print('\n\t3-9\n\n我想去' + str(len(places)) + '个地方。')   #确定列表长度的函数

#3-10、3-11略