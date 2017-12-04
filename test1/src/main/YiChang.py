import sys

'''while True:
    try:
        #x=int(input('输入个数字'))
        break
    except ValueError:
        print('输入有误')

try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('os error:{}'.format(err))
    print("unknow error:",sys.exc_info())
except ValueError:
    print('转数字异常')
except:
    print("unknow error:",sys.exc_info()[0])
    raise


for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:
        print('1')
        print(arg,'has',len(f.readline()),'lines')
        f.close()
'''

try:
    raise NameError('hithere')
except NameError:
    print('An exception flew by!')
    raise
