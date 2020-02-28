import os

message1 = '该目录已存在'
message2 = '错误的目录名'
DIR = 'testdir*（）！&（）'

home = os.path.expanduser('~')
print(home)
try:
    if not os.path.exists(os.path.join(home, DIR)):
        os.makedirs(os.path.join(home, DIR))
    else:
        print(message1)
except Exception as e:
    print(message2)
    print(e)

