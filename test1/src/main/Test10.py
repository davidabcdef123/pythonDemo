sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site=='Runoob':
        print('菜鸟教程')
        # break
    print("循环数据"+site)
else:
        print("没有循环数据")
print("完成循环")

for i in range(5):
    print(i)

for i in range(5,9):
    print(i)

for i in range(0,10,1):
    print(i)

for i in range(-10,-100,-30):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i]);

print(list(range(5)))

for letter in 'runoob':
    if letter=='b':
        break
    print('当前字母为',letter)

var =10
while var>0:
    print('当前变量为：',var)
    var =var-1
    if var==5:
        break
print('88')

for letter in 'runoob':
    if letter=='o':
        continue
    print("当前字母：",letter)

var =10
while var >0:
    var =var-1
    if var==5:
        continue
    print('当前变量：',var)
print('88')

print('----------------------------------')
for n in range(1,10):
    print('n=',n)
    for x in range(2,n):
        if n%x==0:
            print(n,'等于',x,'*',n/x)
            break
    else:
        print(n,'是质数')

for letter in 'runoob':
    if letter =='o':
        pass
        print('执行pass块')
    print('当前字母：',letter)