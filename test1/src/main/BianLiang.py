counter =100
miles=1000.0
name="john"

print(counter)
print(miles)
print(name)
a=b=c=1
a,b,c=1,2,"john"

var1=1
var2=10
del var1,var2
#print(var1)

#元祖
tuple=('',786,2.23,'john',70.2)
tinytuple=(123,'john')
print(tuple)
print((tuple[0]))
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)
#數組
list=['runoob',768,2.33,'john',70.2]
#tuple[2]=1000# 元组中是非法应用
print(list)
list[2]=1000# 列表中是合法应用
print(list)

#字典
dict={}
dict['one']="this is one"
dict[2]="thsi is two"
tinydict={"name":"john",'code':6734,'dept':'sales'}
print(dict['one'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

