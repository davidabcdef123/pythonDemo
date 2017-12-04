class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
finally:
    print('123')

with open('myfile.txt') as f:
    for line in f:
        print(line,end="")