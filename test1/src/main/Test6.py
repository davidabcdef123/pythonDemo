
list1=['googel','runoob',1997,2000];
list2=[1,2,3,4,5,6,7]
print('list[0]=',list1[0])
print('list2[1:5]=',list2[1:5])
print('list1=',list1)
del list1[2]
print('del list1=',list1)

squares = [1, 4, 9, 16, 25]
squares +[36, 49, 64, 81, 100]
print('squares=',squares)
a=['a','b','c']
n=[1,2,3]
x=[a,n]
print('x=',x)
ss={1,2}

tup1 = (50)
type(tup1)     # 不加逗号，类型为整型


tup1 = (50,)
type(tup1)     # 加上逗号，类型为元组

tup1=('googel','runoob',1997,2000)
tup2=(1,2,3,4,5,6,7)

print("tup[0]="+tup1[0])
print('tup2[1:5]=',tup2[1:5])
tup3 =tup1+tup2
print(tup3)

tup=('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print('删除后=')
print(tup)
