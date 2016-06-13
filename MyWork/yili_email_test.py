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


def export_excel_file_daily(v_date):
    # Oracle查询SQL
    sql_file = open('D:\WORK\BBG\JOB\伊利\daily_report.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '

    # 日期参数
    v_year = int(v_date[0:4])
    v_month = int(v_date[5:7])
    v_day = int(v_date[8:10])

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
    v_file_name = path + 'YM_' + v_date + '.xlsx '

    workbook = xlsxwriter.Workbook(v_file_name)
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
    print(v_file_name)


# 发送邮件
def send_email_daily(v_date):
    # 构造邮件头和正文
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'tigeryangjin@gmail.com'
    msg['to'] = '1370365906@qq.com'
    msg['subject'] = 'YM_' + v_date
    content = '''发送自Python '''  # 邮件正文
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    # 构造附件
    attachment_name = 'YM_' + v_date + '.xlsx'  # 附件名称
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
        smtp.sendmail('tigeryangjin@outlook.com', '1370365906@qq.com', str(msg))  # 发送邮件
        smtp.quit()
        print('邮件发送成功！')
        input()
    except Exception as e:
        print(Exception, ":", e)
        send_email_daily(v_date)


def yili_email_daily(v_date):
    # 导出xlsx文件到磁盘
    export_excel_file_daily(v_date)
    # 导出文件作为附件发送邮件
    send_email_daily(v_date)


yili_email_daily(input('请输入日期（格式：yyyy-mm-dd）: '))
