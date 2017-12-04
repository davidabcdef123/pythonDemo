class MyClass:
    i=123456
    def f(self):
        return 'hello'


x=MyClass()
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0,-4.5)
print(x.r,x.i)



class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t=Test()
t.prt()

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
t=Test()
t.prt()

class people:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print('%s 说： 我%d 岁。'%(self.name,self.age))

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print('%s 说：我%d岁了,在读%d年级'%(self.name,self.age,self.grade))
#p=people('tom',12,12)
#p.speak()
s=student('tom',12,16,17)
s.speak()

class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print('我叫%s,我说的主题是 %s'%(self.name,self.topic))

class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test=sample('tom',25,80,4,'python')
test.speak()

#方法重写
class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):
    def myMethod(self):
        print('调用自雷方法')

c=Child()
c.myMethod()

class JustCounter:
    __secretCount=0
    publicCount=0

    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)

counter=JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
#print(counter.__secretCount)

class Site:
    def __init__(self,name,url):
        self.name=name
        self.__url=url

    def who(self):
        print('name:',self.name)
        print('url:',self.__url)

    def __foo(self):
        print('私有')

    def foo(self):
        print('工友')
        self.__foo()

s=Site('菜鸟教程', 'www.runoob.com')
s.who()
s.foo()
#s.__foo()

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'vertor(%d,%d)'%(self.a,self.b)

    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)








