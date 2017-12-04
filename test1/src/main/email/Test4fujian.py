import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender='xxxxxxxxx@xxxxxxxxx'
receivers=['xxxxxxxxxxxx@qq.com']

message=MIMEMultipart()
message['From']=Header('菜鸟教程','utf-8')
message['To']=Header('测试','utf-8')
subject='phton邮件测试'
message['Subject']=Header(subject,'utf-8')
#邮件正文内容
message.attach(MIMEText('走你', 'plain', 'utf-8'))

# 构造附件1， 文件
att1=MIMEText(open('D:\data\logs\zxxxxx.xxxxx.xxxxxx\default.log','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
#这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2， 文件
att2 = MIMEText(open('D:\data\logs\zxxxxxxx.xxxxxxx.xxxxxxxxx\default.log.2017-08-07', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)



try:
    smtpObj=smtplib.SMTP('smtps.xxxxxxxxxxxx.com.cn')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except:
    print('错误')