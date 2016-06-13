import smtplib
import email.mime.multipart
import email.mime.text
import time
import schedule


def send_email():
    # 构造邮件头和正文
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'tigeryangjin@gmail.com'
    msg['to'] = '1370365906@qq.com'
    msg['subject'] = 'hello,yangjin'+str(time.time())
    content = '''发送自Python '''  # 邮件正文
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 构造附件
    # attachment_name = v_file_name  # 附件名称
    # att1 = email.mime.text.MIMEText(open('D:\WORK\BBG\JOB\伊利\表格\\' + attachment_name, 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=' + attachment_name  # 邮件显示的附件名称
    # msg.attach(att1)

    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp-mail.outlook.com', '25')  # 连接到发邮件服务器 端口：25、587
        smtp.starttls()  # 开启TLS/SSL加密
        smtp.login('tigeryangjin@outlook.com', 'tiger19790909')  # 登录邮箱
        smtp.sendmail('tigeryangjin@outlook.com', '12109471@qq.com', str(msg))  # 发送邮件
        smtp.quit()
        print('邮件发送成功！')
    except Exception as e:
        print(Exception, ":", e)
        send_email()


schedule.every(1).minutes.do(send_email)


# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
