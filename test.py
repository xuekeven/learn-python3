
print('\n\t10-1\n')
file_path = 'D:/Learn/Python/Basis/learning_python.txt'   #使用绝对路径打开文件，路径前加r表示rawstring（原生字符串）

with open(file_path) as file_object:   #函数默认为只读模式('r')
    contents = file_object.read()   #方法读取整个文件并且保存在变量中
    print(contents)   #read()阅读