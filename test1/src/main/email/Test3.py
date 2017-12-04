import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host="smtps.qq.com.cn"
mail_user="xxxxxxxxx@xxxxxxxxxxxx"
mail_pass="aaaaaaaaaaaaa"

sender='xxxxxxxxxxxxx@xxxxxxxxxx'
receivers=['xxxxxxxxxxxxx@qq.com']
mail_msg="""
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message=MIMEText(mail_msg,'html','utf-8')
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