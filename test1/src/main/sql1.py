import pymysql as pymysql

db=pymysql.connect("localhost","root","1234","jeesite" )

cursor=db.cursor()

cursor.execute('select version()')

data=cursor.fetchone()

print("Database version : %s " % data)
print(cursor)

sql='insert into test1(id) values(2)'
'''sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Mac', 'Mohan', 20, 'M', 2000)'''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


sql='select * from sys_menu'
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        a=row[0]
        b=row[1]
        print(a,b)
except:
    print('S')

db.close()