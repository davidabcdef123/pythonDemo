num=int(input('输入一个数字'))
if num%2==0:
    if num%3==0:
        print('23都可以')
    else:
        print('可以整除2，但不能3')
else:
    if num%3==0:
        print('可以整除3单不能整除2')
    else:
        print('23都不想')