import datetime
import doctest
import os

#print(os.getcwd())

#os.chdir('/server/accesslogs')
#os.system('mdir today')

#print(dir(os))
#print(help(os))
#help(os)
import sys
from timeit import Timer

from urllib.request import urlopen

import zlib

print(sys.argv)

'''for line in urlopen('http://www.baidu.com'):
    line =line.decode('utf-8')
    print(line)'''

now= datetime.date.today()
print(now)

datetime.date(2003,12,2)
print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))

birthday= datetime.date(1964, 7, 31)
age=now-birthday
print(age.days)

s=b'witch which has which witches wrist watch'
print(len(s))
t=zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    print(average([20, 30, 70]))
    return sum(values) / len(values)
doctest.testmod()