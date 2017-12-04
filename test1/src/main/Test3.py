# help(max.__doc__)
# !/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

a = b = c = 1
# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。


# 您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

'''
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
'''

str = 'Runoob'
print(str)
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "test")

print('Ru\noob')
print(r'Ru\noob')
print('你好')
print('hello');
print('123')

if True:
    print("true")
else:
    print("false")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    # 没有严格缩进，在执行时会报错
print("False")



'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""


import sys;x='123456';sys.stdout.write(x)

x="a"
y="b"
print(x)
print(y)
#不換行
print(x,),
print(y,),

print (x,y)