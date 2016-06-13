# Python3.5
# -*- coding: utf-8 -*-
# Author by YangJin

import cx_Oracle
import os
import xlsxwriter
import smtplib
import email.mime.multipart
import email.mime.text
import datetime

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码

# v_file_name导出文件名为全局变量
v_file_name = ''


def yili_daily():
    # 每日销售数据
    v_date = input('请输入日期（格式：yyyy-mm-dd，默认值为昨天）:\n ')
    if v_date == '':
        v_in_date = str(datetime.date.today() - datetime.timedelta(days=1))
    else:
        v_in_date = v_date
    # Oracle查询SQL
    sql_file = open('D:\WORK\BBG\JOB\伊利\daily_report.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '

    # 日期参数
    v_year = int(v_in_date[0:4])
    v_month = int(v_in_date[5:7])
    v_day = int(v_in_date[8:10])

    # 配置信息
    try:
        conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
        cursor = conn.cursor()
        cursor.execute(sql_text, {'TODAY': datetime.date(v_year, v_month, v_day)})  # 传入日期参数
        sql_result = cursor.fetchall()
        cursor.close()
        conn.close()
        print('SQL查询完成！')
    except Exception as e:
        print(Exception, ":", e)

    # 生成excel文件-------------------------------------------------------
    # 生成excel文件名
    path = 'D:\WORK\BBG\JOB\伊利\表格\\'
    global v_file_name
    v_file_name = 'YM_' + v_in_date + '.xlsx '
    v_file_path = path + v_file_name

    workbook = xlsxwriter.Workbook(v_file_path)
    # 创建
    worksheet = workbook.add_worksheet()

    # Add an Excel date format.
    date_format = workbook.add_format({'num_format': 'yyyy/mm/dd', 'font_size': 9, 'font_name': '宋体'})
    head_format = workbook.add_format({'bold': 1, 'font_size': 9, 'font_name': '宋体'})
    data_format = workbook.add_format({'font_size': 9, 'font_name': '宋体'})

    # 写入列名
    worksheet.write(0, 0, '销售日期', head_format)
    worksheet.write(0, 1, '去年同期日期', head_format)
    worksheet.write(0, 2, '小类', head_format)
    worksheet.write(0, 3, '小类名称', head_format)
    worksheet.write(0, 4, '供应商编码', head_format)
    worksheet.write(0, 5, '供应商名称', head_format)
    worksheet.write(0, 6, '门店编码', head_format)
    worksheet.write(0, 7, '门店名称', head_format)
    worksheet.write(0, 8, '业态', head_format)
    worksheet.write(0, 9, '区域', head_format)
    worksheet.write(0, 10, '商品', head_format)
    worksheet.write(0, 11, '商品名称', head_format)
    worksheet.write(0, 12, '销售数量', head_format)
    worksheet.write(0, 13, '销售成本', head_format)
    worksheet.write(0, 14, '销售金额', head_format)
    worksheet.write(0, 15, '毛利额', head_format)
    worksheet.write(0, 16, '去年销售量', head_format)
    worksheet.write(0, 17, '去年销售成本', head_format)
    worksheet.write(0, 18, '去年销售金额', head_format)
    worksheet.write(0, 19, '去年毛利额', head_format)
    for r in range(len(sql_result)):
        for c in range(len(sql_result[r])):
            if c in (0, 1):  # 第一、二列为日期格式
                worksheet.write(r + 1, c, sql_result[r][c], date_format)

            else:
                worksheet.write(r + 1, c, sql_result[r][c], data_format)
    workbook.close()
    print('导出到xlsx文件成功！')
    print(v_file_path)


def yili_dq_215():
    # 伊利215中类档期数据
    v_bdate = input('请输入开始日期（格式：yyyy-mm-dd）:')
    v_edate = input('请输入结束日期（格式：yyyy-mm-dd）:')
    # Oracle查询SQL
    sql_file = open('D:\WORK\BBG\JOB\伊利\DQ_yili_215.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '

    # 日期参数
    v_byear = int(v_bdate[0:4])
    v_bmonth = int(v_bdate[5:7])
    v_bday = int(v_bdate[8:10])
    v_eyear = int(v_edate[0:4])
    v_emonth = int(v_edate[5:7])
    v_eday = int(v_edate[8:10])

    # 配置信息
    try:
        conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
        cursor = conn.cursor()
        cursor.execute(sql_text, {'BDATE': datetime.date(v_byear, v_bmonth, v_bday),
                                  'EDATE': datetime.date(v_eyear, v_emonth, v_eday)})  # 传入日期参数
        sql_result = cursor.fetchall()
        cursor.close()
        conn.close()
        print('SQL查询完成！')
    except Exception as e:
        print(Exception, ":", e)

    # 生成excel文件-------------------------------------------------------
    # 生成excel文件名
    path = 'D:\WORK\BBG\JOB\伊利\表格\\'
    global v_file_name
    v_file_name = 'DQ_' + v_bdate + '~' + v_edate + '.xlsx '
    v_file_path = path + v_file_name

    workbook = xlsxwriter.Workbook(v_file_path)
    # 创建
    worksheet = workbook.add_worksheet()

    # Add an Excel date format.
    # date_format = workbook.add_format({'num_format': 'yyyy/mm/dd', 'font_size': 9, 'font_name': '宋体'})
    head_format = workbook.add_format({'bold': 1, 'font_size': 9, 'font_name': '宋体'})
    data_format = workbook.add_format({'font_size': 9, 'font_name': '宋体'})

    # 写入列名
    worksheet.write(0, 0, '门店编码', head_format)
    worksheet.write(0, 1, '门店名称', head_format)
    worksheet.write(0, 2, '商品', head_format)
    worksheet.write(0, 3, '商品名称', head_format)
    worksheet.write(0, 4, '供应商编码', head_format)
    worksheet.write(0, 5, '供应商名称', head_format)
    worksheet.write(0, 6, '销售数量', head_format)
    worksheet.write(0, 7, '销售成本', head_format)
    worksheet.write(0, 8, '销售金额', head_format)
    worksheet.write(0, 9, '毛利额', head_format)
    for r in range(len(sql_result)):
        for c in range(len(sql_result[r])):
            worksheet.write(r + 1, c, sql_result[r][c], data_format)
    workbook.close()
    print('导出到xlsx文件成功！')
    print(v_file_name)


def yili_month_215():
    pass


def send_email(v_file_name):
    # 构造邮件头和正文
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'tigeryangjin@gmail.com'
    msg['to'] = '1370365906@qq.com'
    msg['subject'] = v_file_name
    content = '''发送自Python '''  # 邮件正文
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 构造附件
    attachment_name = v_file_name  # 附件名称
    att1 = email.mime.text.MIMEText(open('D:\WORK\BBG\JOB\伊利\表格\\' + attachment_name, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=' + attachment_name  # 邮件显示的附件名称
    msg.attach(att1)

    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp-mail.outlook.com', '25')  # 连接到发邮件服务器 端口：25、587
        smtp.starttls()  # 开启TLS/SSL加密
        smtp.login('tigeryangjin@outlook.com', 'tiger19790909')  # 登录邮箱
        smtp.sendmail('tigeryangjin@outlook.com', '12109471@qq.com', str(msg))  # 发送邮件
        smtp.quit()
        print('邮件发送成功！')
        input()
    except Exception as e:
        print(Exception, ":", e)
        send_email(v_file_name)


def top_level():
    # 伊利邮件总函数
    msg = input('请选择要发送的邮件:\n'
                '[0] 每日销售 \n'
                '[1] 伊利215中类档期销售 \n'
                '[2] 伊利215中类月汇总销售 \n'
                '-------------------------\n')
    if msg == '0':
        # [0] 每日销售
        yili_daily()
        send_email(v_file_name)
    elif msg == '1':
        # [1] 伊利215中类档期销售
        yili_dq_215()
        send_email(v_file_name)
    elif msg == '2':
        # [2] 伊利215中类月汇总销售
        print('待开发。。。')
    else:
        print('输入错误！')
        top_level()


top_level()
