
#9.1 创建和使用类

#9-1 & 9-4

print('\n\t9-1 & 9-4\n')
class Restaurant():   #创建实例（类），注意冒号，区分大小写

    def __init__(self,restaurant_name,cuisine_type):   #类中的函数称为方法，__init__为特殊方法，每次都会被调用且必须含形参self用来指向实例本身
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers = 0   #属性可以创建类时作为形参赋予，也可以在函数中定义，但属性必须得有默认值
        self.number_max = 0
        self.number_served = 0
        print('Welcome to our restaurant!')

    def describe_restaurant(self):
        print("Our restaurant's name is " + self.restaurant_name +'.')
        print("Our resraurant's cuisint type is  " + self.cuisine_type + '.')

    def open_restaurant(self):
        print('Our restaurant open at 9:00-23:30.')

    def set_number_served(self,max):
        self.number_max = max   #通过方法修改属性的值
        print('We can hold ' + str(self.number_max) + ' people at most on one table. ')

    def increate_number_served(self,num):
        self.number_served += num   #通过方法对属性的值进行递增

    def restaurant_served(self):
        print('We have served ' + str(self.number_served) + ' people.')

my_restaurant = Restaurant('Kai','Chinese')   #创建实例，只运行第一个基础的__init__方法（函数）
print(my_restaurant.restaurant_name)   #访问实例的属性
my_restaurant.number_served = 100   #直接修改属性的值
my_restaurant.describe_restaurant()   #调用实例的方法
my_restaurant.open_restaurant()
my_restaurant.restaurant_served()
my_restaurant.set_number_served(8)
my_restaurant.increate_number_served(100)
my_restaurant.restaurant_served()


#9-2略
#9-3

print('\n\t9-3\n')
class User():   

    def __init__(self,first_name,last_name,**infor):   #建立空字典面对未知实参，已知为字典不必加**
        self.first_name = first_name
        self.last_name = last_name
        self.infor = infor

    def describe_user(self):
        for key,valus in self.infor.items():
            print(key.title() + ':' +valus)

    def greet_user(self):
        print('Hello, ' + self.first_name  + ' ' + self.last_name + ' Good luck!' )

user1 = User('Xue','Kai',age = '22',height = '174cm')
user1.greet_user()
user1.describe_user()

#9.2 使用类和实例

#9-5略

#9.3 继承

#9-6

print('\n\t9-6\n')
class IceCreamStand(Restaurant):   #继承类时子类和父类需在同一文件
    def __init__(self,restaurant_name,cuisine_type):   #定义子类时必须括号内指定父类的方法
        super().__init__(restaurant_name,cuisine_type)   #特殊函数super()将子类与父类关联，子类需父类的属性时须在括号内标注
        self.flavors = []   #给子类定义属性
    
    def increate_flavors(self,flavor):   #给子类定义方法
        self.flavors.append(flavor)
    
    def print_orders(self):
        print('There are our flavors:')
        for a in self.flavors:
            print(a.title())
    def open_restaurant(self):   #重写父类的方法，需要与父类重名
        print('Our restaurant open at 9:00-22:00.')

icecream = IceCreamStand('Wang','Ice')
icecream.describe_restaurant()
icecream.increate_flavors('apple')
icecream.increate_flavors('banana')
icecream.open_restaurant()
icecream.print_orders()

#9-7 & 9-8

print('\n\t9-7 & 9-8\n')
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for show in self.privileges:
            print(show)

class Admins(User):
    def __init__(self,first_name,last_name,**infor):
        super().__init__(first_name,last_name,**infor)
        self.priv = Privileges()   #将实例用作属性，被用的实例需在前

Admin = Admins('The','User',age = '1998')
Admin.priv.show_privileges()   #调用被实例用作属性的属性

#9-9略

#9.4 导入类

import car   #导入整个模块
my_beetle = car.Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name()) 

from car import Car   #从模块导入单个类
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

from car import Car,ElectricCar   #从模块导入多个类
my_beetle = Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name()) 
my_tesla = ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())

from module_name import *   #从模块导入所有类

#9-10、9-11、9-12略

#9.5 python标准库

#9-13、9-14、9-15略

#9.6 类编码风格