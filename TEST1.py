import email.mime.multipart
import email.mime.text


def send_email(v_date):
    # 构造邮件头和正文
    msg = email.mime.multipart.MIMEMultipart()
    print(msg, '\n***************************\n')
    msg['from'] = 'tigeryangjin@gmail.com'
    print(msg, '\n***************************\n')
    msg['to'] = '1370365906@qq.com'
    print(msg, '\n***************************\n')
    msg['subject'] = 'YM_' + v_date
    print(msg, '\n***************************\n')
    content = '''发送自Python '''  # 邮件正文
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    print(msg, '\n***************************\n')


send_email('2016-06-05')
