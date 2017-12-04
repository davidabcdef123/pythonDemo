f = open("d:/testaaa.txt", "r")
#str=f.read()
#print(str)


#for line in f:
#    print(line,end='')

f = open("d:/testaaa.txt", "w")
num=f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)


f = open("d:/tmp/foo1.txt", "w")
value=('www.runoob.com',14)
s=str(value)
f.write(s)

f = open('d:/tmp/foo1.txt', 'rb+')
f.write(b'0123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))


f.close()