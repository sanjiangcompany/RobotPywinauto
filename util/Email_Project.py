# ******************发送邮件脚本**********************************
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# file_path = r"D:\RobotAutomation\report\result.html" 这个本地文件的绝对路径编写如下：
BATH_PATH = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BATH_PATH, r'report\result.html')

# ----------1.跟发邮件相关的参数------
class Email:
    # smtpserver = "smtp.163.com"           # 发件服务器
    # port = 465                            # 端口

    smtpserver = "smtp.126.com"  # 发件服务器
    port = 994  # 端口
    # sender = 'zhaoshan950602@163.com'   # 读取配置文件中发件人
    # sendpwd = 'JYRRLTHENMUIXTUA'    # 读取配置文件中发件人密码，这个是邮箱授权码

    # sender = '15936558246@163.com'
    # sendpwd = 'UTJWEOILMFOGJHOS'

    sender = 'zhaoshan950602@126.com'
    sendpwd = 'HIVYCIRVENCQRBKW'

    # receiver = ['zhaoshan950602@126.com']
    receiver = ['luzhaoshan@encootech.com', 'zhaoshan950602@126.com']  # 读取配置文件中收件人

    # ----------2.编辑邮件的内容------
    # 读文件
    import time
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    with open(file_path, "rb") as fp:
        # print(file_path)
        mail_body = fp.read()

    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = ";".join(receiver)  # 多个收件人list转str
    msg["subject"] = "【Robot】BVT测试报告"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, sendpwd)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, sendpwd)  # 登录

    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
