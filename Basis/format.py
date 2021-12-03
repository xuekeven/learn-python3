#   str.format()用法

#位置参数


print("{}的性别是：{}".format("小明","男"))   #不设置指定位置，按默认顺序


print("{0} {1}".format("Hello","World"))   #设置指定位置
print("{1} {0}".format("Hello","World"))   #设置指定位置
print("{0} {1} {0}".format("Hello","World"))   #设置指定位置
print("{1} {1} {0}".format("Hello","World"))   #设置指定位置


list1 = ["Hello","World"]   #通过序列传入

print("{} {}".format(*list1))   #按照默认位置传入
print("{0} {1}".format(*list1))   #按照指定位置传入
print("{1} {0}".format(*list1))   #按照指定位置传入

#关键字参数


print("{name}的身高是{height}".format(name="小明",height="180cm"))   #直接传入

asd = {"name":"小明","height":"180cm"}   #通过字典传入
print("{name}的身高是{height}".format(**asd))


#格式化数字


grade = 97.556   
print("我的成绩为：{:.2f}分".format(grade))   #格式化数字：https://www.runoob.com/python/att-string-format.html


