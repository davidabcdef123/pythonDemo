from collections import deque


a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333),a.count(66.25),a.count('x'))

a.insert(2,-1)
a.append(333)
print(a)

print(a.index(333))

a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack.pop())
print(stack.pop())
print(stack)

queue=deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue)

vec=[2,4,6]
print([3*x for x in vec])
print([[x,x**2] for x in vec])

#freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
#1print([weapon.strip() for weapon in freshfruit])

print([3*x for x in vec if x>3])

vec1=[2,4,6]
vec2=[4,3,9]
print([x*y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

print([str(round(355/133,i) for i in range(1,6))])

matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],]
print([row[i] for row in matrix] for i in range(4))

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

a= [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)
del a[:]
print(a)

t=12345,54321,'hello'
print(t[0])
print(t)
u=t,(1,2,3,4,5)
print(u)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('adsfse' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)# a 中唯一的字母
print(a-b)# 在 a 中的字母，但不在 b 中
print(a|b) # 在 a 或 b 中的字母
print(a&b)
print(a^b)# 在 a 或 b 中的字母，但不同时在 a 和 b 中

tel = {'jack': 4098, 'sape': 4139}
tel['guido']=4127
print(tel)
tel['irv']=4127
print(tel)
print(list(tel.keys()))
del tel['sape']
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1,10,2)):
    print(i)






