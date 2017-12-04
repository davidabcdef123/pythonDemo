dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

dict11={'abc':123,986:14}

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict[name]=",dict['Name'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age']=8 #更新age
dict['school']="菜鸟教程" #添加信息
print('dict["age"]=',dict['Age'])
print('dict["school"]=',dict['school'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['Name']
dict.clear()
del dict
#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(type(dict))