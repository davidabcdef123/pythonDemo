import smtplib
from email.header import Header
from email.mime.text import MIMEText

sender='XXXXXX@XXXXX'
receivers=['xxxxxxxxxx@qq.com']
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message=MIMEText('邮件发送，走你','plain','utf-8')
message['From']=Header('菜鸟教程','utf-8')
message['To']=Header('测试','utf-8')

subject='phton邮件测试'
message['subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP('smtps.qq.com.cn')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print("发送失败")