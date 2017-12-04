import time

import _thread


def print_time(threanName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print('%s : %s'%(threanName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,('thread-1',2,))
    _thread.start_new_thread(print_time,('thread-2',4,))

except Exception as e:
    print(e)

while 1:
    pass