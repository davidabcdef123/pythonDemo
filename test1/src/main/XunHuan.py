n=100

sum=0
counter=1
while counter<=n:
    sum+=counter
    counter+=1
print('1到 %d 之和为： %d'%(n,sum))


num=1
#while num==1:
 #   num2=int(input("输入一个数字："))
  #  print('你输入的数字是：',num2)
print("666")

count=0
while count<5:
    print(count,'小于5')
    count=count+1
else:
    print(count,'>或=5')

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site=='Runoob':
        print('菜鸟教程');
       # break
    print("循环数据"+site)
else:
    print("没有循环数据")
print("完成循环")