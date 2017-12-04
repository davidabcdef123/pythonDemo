x="a"
y="b"
print(x)
print(y)

print("--------------------------")

print( x, end=" " )
print( y, end=" " )

import sys
print('--------------------------------------------')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)

from sys import argv,path

print('============================from import====================================')
print('path',path)

'''
    1
    2
    3
'''

help(max.__doc__)