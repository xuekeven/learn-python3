
#11.1 测试函数

#11-1 # 11-2
'''
编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式
为 City, Country 的字符串，如 Santiago, Chile。将这个函数存储在一个
名为 city _functions.py 的模块中。创建一个名为 test_cities.py 的程序，对
刚编写的函数进行测试（别忘了，你需要导入模块 unittest 以及要测试的函数）。
编写一个名为 test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用
前述函数时，得到的字符串是正确的。运行 test_cities.py，确认测试 test_city_country()通过了。
'''
print('\n\t11-1 & 11-2\n')   
def hanshu(city,country,population=''):
    if population:
        zifuchuan = city + ',' + country + ' - ' + population
    else:
        zifuchuan = city + ',' + country
    return zifuchuan

print("\nPlease Enter 'q' at any time to quit." )
while True:
    city = input("Give us the city's name.")
    if city == 'q':
        break
    country = input("Give us the country's name.")
    if country == 'q':
        break

    infor = hanshu(city,country)
    print('The infor:' + infor)

import unittest   #引入测试模块

class Test_city_country(unittest.TestCase):

    def test_city_country(self):   #方法必须以test_打头
        test = hanshu('sanya','china')   #调用函数并返回值
        self.assertEqual(test,'sanya,china')   #使用断言方法比较

    def test_city_country_population(self):   #添加测试
        test = hanshu('huashengdun','usa','10000')
        self.assertEqual(test,'huashengdun,usa - 10000')

unittest.main()   #运行测试文件

#11.2 测试类

#11-3
'''
编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为 give_raise()的方法，它默认将年薪增加 5000美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_ raise()
和 test_give_custom_raise()。使用方法 setUp()，以免在每个测试方法中都创建新的雇员实例。
运行这个测试用例，确认两个测试都通过了。
'''

print('\n\t11-3\n')
import unittest
class Employee():

    def __init__(self,first,last,money):
        self.first = first
        self.last = last
        self.money = money

    def give_raise(self,more=5000):
        self.money += more

    def end_money(self):
        infor = self.first + ' ' + self.last + ': ' + str(self.money) 
        return infor

class TestEmployee(unittest.TestCase):

    def setUp(self):   #避免测试时重复创建新实例，创建公用的调查对象和答案列表
        self.my_money = Employee('Xue','Kai',10000)
        self.moremoneys = [10000,20000]
        self.gomoneys = [20000,40000]
        self.numbers = [0,1]

    def test_give_default_raise(self):
        self.my_money.give_raise(1000)
        my_infor = self.my_money.end_money()
        self.assertEqual('Xue Kai: 11000',my_infor)
    
    def test_give_custom_raise(self):
        for num in self.numbers:
            self.my_money.give_raise(self.moremoneys[num])
            self.assertEqual( 'Xue Kai: ' + str(self.gomoneys[num]),self.my_money.end_money())

unittest.main()





