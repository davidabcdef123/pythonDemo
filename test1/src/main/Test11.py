def printme(str):
    print(str)
   # return

printme('123')
#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

def changeme(mylist):
    mylist.append([1,2,3,4])
    print("内=",mylist)
    return

mylist=[10,20,30]
changeme(mylist)
print('外=',mylist)

def printme(str):
    print(str)
    return
printme(str='123')

def printinfo(name,age):
    print ("名字: ", name);
    print ("年龄: ", age);
    return;
printinfo(age=50,name='runoob')

def printinfo(name,age=35):
    print ("名字: ", name);
    print ("年龄: ", age);
    return;
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );

def printinfo(arg1,*vartuple):
    print('输出')
    print(arg1)
    for var in vartuple:
        print(var)

printinfo(10)
printinfo(10,20,30)

sum=lambda arg1,arg2:arg1+arg2;

print('和',sum(10,20))

def sum(arg1,arg2):
    return arg1+arg2
total=sum(10,20)
print(total)

x = int(2.9)  # 内建作用域

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

if True:
    msg='1'
print(msg)

num=1
def fun1():
    global num
    print(num)
    num=12312312321
    print(num)
fun1()

def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)
outer()

