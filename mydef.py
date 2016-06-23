# 支付宝2.15亿奖金平分
def zfb(min_person, max_person, total_amt):
    import matplotlib.pyplot as plt
    ind = []
    dif = []
    for p in range(min_person, max_person):
        ind.append(p)
        dif_amt = round(p * (total_amt / p - round(total_amt / p, 2)), 2)
        dif.append(dif_amt)
    for i in range(max_person - min_person):
        print(ind[i], dif[i])
    plt.scatter(ind, dif)
    plt.show()


def writer_to_csv():
    import csv

    with open("XXX.csv", "w", newline="") as datacsv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvwriter.writerow(["A", "B", "C", "D"])


def write_file():
    '''
    Created on Dec 18, 2012
    写入文件
    @author: liury_lab
    '''
    # 最简单的方法
    all_the_text = 'hello python'
    open('d:/text.txt', 'w').write(all_the_text)
    all_the_data = b'abcd1234'
    open('d:/data.txt', 'wb').write(all_the_data)
    # 更好的办法
    file_object = open('d:/text.txt', 'w')
    file_object.write(all_the_text)
    file_object.close()
    # 分段写入
    list_of_text_strings = ['hello', 'python', 'hello', 'world']
    file_object = open('d:/text.txt', 'w')
    for string in list_of_text_strings:
        file_object.writelines(string)
    list_of_text_strings = ['hello', 'python', 'hello', 'world']
    file_object = open('d:/text.txt', 'w')
    file_object.writelines(list_of_text_strings)


# 学生成绩class
class StudentsScore:
    def __init__(self, name, homework, quizzes, tests):
        self.name = name
        self.homework = homework
        self.quizzes = quizzes
        self.tests = tests

    # Add your function below!
    def average(self):
        total = float(sum(self))
        l = len(self)
        avg = total / l
        return avg

    def get_average(self):
        homework = StudentsScore.average(self.homework)
        quizzes = StudentsScore.average(self.quizzes)
        tests = StudentsScore.average(self.tests)
        return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

    def get_letter_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"


# 斐波那契数列 方法一
def fibonacci(m):
    list1 = []
    list1.append(0)
    list1.append(1)
    a, b = 0, 1
    for i in range(m):
        a = a + b
        if len(list1) < m:
            list1.append(a)
            b = a + b
            if len(list1) < m:
                list1.append(b)
            else:
                break
        else:
            break
    return list1


# 斐波那契数列 方法二
def fib(m):
    fibs = [0, 1]
    num = m
    for i in range(int(num) - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


# 以需要的时间间隔执行某个命令
def re_exe(cmd, inc=3):
    import time
    import os
    while True:
        os.system(cmd)
        time.sleep(inc)


def plt_scatter():
    from numpy import random, ones, array
    import matplotlib.pyplot as plt
    a = random.randint(0, 50, 50)
    b = random.randint(0, 50, 50)
    fig = plt.figure(1)
    plt.subplot(211)
    plt.scatter(a, b)

    # with label
    plt.subplot(212)
    label = list(ones(20)) + list(2 * ones(15)) + list(3 * ones(15))
    label = array(label)
    # 画图，最后二个参数为颜色参数。
    # label数据类型为numpy.ndarray，有三种值（1，2，3）
    plt.scatter(a, b, 15.0 * label, 15.0 * label)
    plt.show()
    print(label)


def matrix_mcl():
    import numpy as np
    a = np.arange(20).reshape(4, 5)
    # a = [[20, 5], [15, 10]]
    a = np.asmatrix(a)
    b = np.arange(2, 45, 3).reshape(5, 3)
    # b = [[2, 1], [1, 4]]
    b = np.mat(b)
    print("matrix a:")
    print(a)
    print("matrix b:")
    print(b)
    c = a * b
    print("matrix c:")
    print(c)


def schedule_email():
    # 定时发送邮件
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
        msg['subject'] = 'hello,yangjin' + str(time.time())
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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    """模拟队列"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
