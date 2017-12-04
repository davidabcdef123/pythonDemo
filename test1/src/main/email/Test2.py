import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host="smtps.qq.com.cn"
mail_user="xxxxxx@zxxxxxx"
mail_pass="1111111111111"

sender='xxxxxx@xxxxxx'
receivers=['xxxxx@qq.com']

message=MIMEText('邮件发送，走你','plain','utf-8')
message['From']=Header('菜鸟教程','utf-8')
message['To']=Header('测试','utf-8')

subject='phton邮件测试'
message['subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except:
    print('错误')