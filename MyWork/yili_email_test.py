import smtplib
import email.mime.multipart
import email.mime.text

v_file_name = 'D:\WORK\BBG\JOB\伊利\表格\YM_2016-10-10.xlsx'


def send_email(v_file_name):
    # 构造邮件头和正文
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'tigeryangjin@126.com'
    msg['to'] = 'tiger.impost@qq.com'
    msg['subject'] = v_file_name
    content = '''发送自Python '''  # 邮件正文
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 构造附件
    attachment_name = v_file_name  # 附件名称
    att1 = email.mime.text.MIMEText(open(v_file_name, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=' + attachment_name  # 邮件显示的附件名称
    msg.attach(att1)

    # 邮箱:ytbenben147@126.com,1370365906@qq.com
    # 发送邮件_outlook邮箱
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp-mail.outlook.com', '25')  # 连接到发邮件服务器 端口：25、587
        smtp.starttls()  # 开启TLS/SSL加密
        smtp.login('tigeryangjin@outlook.com', 'tiger19790909')  # 登录邮箱
        smtp.sendmail('tigeryangjin@outlook.com', 'ytbenben147@126.com',
                      str(msg))
        smtp.quit()
        print('邮件发送成功！')
        print('执行完毕！')
        input()
    except Exception as e:
        print(Exception, ":", e)
        send_email(v_file_name)

        # 发送邮件_QQ邮箱
        # try:
        #     print('start...')
        #     smtp = smtplib.SMTP()
        #     smtp.connect('smtp.qq.com', '465')  # 连接到发邮件服务器 端口：25
        #     smtp.starttls()  # 开启TLS/SSL加密
        #     smtp.login('tiger.impost@qq.com', 'Tiger@1979!')  # 登录邮箱
        #     smtp.sendmail('tiger.impost@qq.com', 'tigeryangjin@outlook.com', str(msg))
        #     smtp.quit()
        #     print('邮件发送成功！')
        #     print('执行完毕！')
        #     input()
        # except Exception as e:
        #     print(Exception, ":", e)
        #     send_email(v_file_name)


send_email(v_file_name)
