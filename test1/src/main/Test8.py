age=int(input("输入狗的年龄"))
print('')
if age<0:
    print('怎么可能');
elif age ==1:
    print('相当于14')
elif age==2:
    print('相当于22')
elif age>2:
    human=22+(age-2)*5
    print("对应=",human)
input('点击退出')