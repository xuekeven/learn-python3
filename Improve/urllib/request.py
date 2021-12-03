import urllib.request as ur   #导入urllib库的request模块并指定别名
import urllib.parse as up 

'''简单的请求和网页抓取

req = ur.urlopen('https://baidu.com')   #爬取网站并返回HTTPResponse类型对象

print(type(req))
print(req.status)
print(req.getheaders())

mess = req.read().decode('utf-8')   #对HTTPResponse调用方法和属性得到网站相关信息后赋给变量mess

files = 'D:/新建文件夹/New Files/Learn/Python/Improve/urllib/files/word.html'
with open(files,'w',encoding='utf-8') as file:
    file.write(mess)

爬取时传递参数

data = bytes(up.urlencode({'word':'hello'}),encoding = 'utf-8')   #传递参数并转码为字节流类型
res = ur.urlopen('http://httpbin.org/post', data = data,timeout = 5)
print(res.read())
'''

'''更强大的功能'''

url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Widnows NT)',
    'Host':'httpbin.org'
}

dicto = {
    'name':'Germey'
}

data = bytes(up.urlencode(dicto),encoding = 'utf-8')
requ = ur.Request(url = url,data = data,headers = headers,method = 'POST')
resp = ur.urlopen(requ)
print(resp.read().decode('utf-8'))