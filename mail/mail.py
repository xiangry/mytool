#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "mlxiangry@qq.com"
mail_pass = "nsbczuudesqaejcf"

sender = "front_error@super2.com"
receivers = ['xingsheng.gao@kaiqigu.com']

# message = MIMEText('测试Python发送邮件', 'plain', 'utf-8')

message = MIMEMultipart()
message['Form'] = Header('高', "utf-8")
message['To'] = Header('error', "utf-8")

subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('测试Python发送邮件', 'plain', 'utf-8'))

att1 = MIMEText(open("error.log", "rb").read(), 'base64', 'utf-8')
att1['Content-Type'] = "application/octet-stream"
att1['Content-Disposition'] = 'attachment; filename="error.log"'
message.attach(att1)


def mail():
    ret = True
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.debuglevel = True  # 输出信息
        smtpObj.ehlo()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        smtpObj.quit()
    except smtplib.SMTPException:
        ret = False
    return ret

ret = mail()
if ret:
    print "SUCCESS:邮件发送成功", receivers
else:
    print "FAILED:邮件发送失败"


