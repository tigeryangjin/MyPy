# Python3.5
# -*- coding: utf-8 -*-

import cx_Oracle
import os
import xlsxwriter
import smtplib
import email.mime.multipart
import email.mime.text

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码


def export_excel_file(v_date):
    # Oracle查询SQL
    sql_file = open('D:\WORK\BBG\JOB\伊利\daily_report.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '

    # 配置信息
    conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
    cursor = conn.cursor()
    cursor.execute(sql_text)
    sql_result = cursor.fetchall()
    cursor.close()
    conn.close()

    # 生成excel文件-------------------------------------------------------
    # 生成excel文件名
    v_file_name = 'YM_' + v_date + '.xlsx '
    print(v_file_name)
    workbook = xlsxwriter.Workbook(v_file_name)
    # 创建
    worksheet = workbook.add_worksheet()

    # Add an Excel date format.
    date_format = workbook.add_format({'num_format': 'yyyy/mm/dd'})

    # 写入列名
    worksheet.write(0, 0, '销售日期')
    worksheet.write(0, 1, '去年同期日期')
    worksheet.write(0, 2, '小类')
    worksheet.write(0, 3, '小类名称')
    worksheet.write(0, 4, '供应商编码')
    worksheet.write(0, 5, '供应商名称')
    worksheet.write(0, 6, '门店编码')
    worksheet.write(0, 7, '门店名称')
    worksheet.write(0, 8, '业态')
    worksheet.write(0, 9, '区域')
    worksheet.write(0, 10, '商品')
    worksheet.write(0, 11, '商品名称')
    worksheet.write(0, 12, '销售数量')
    worksheet.write(0, 13, '销售成本')
    worksheet.write(0, 14, '销售金额')
    worksheet.write(0, 15, '毛利额')
    worksheet.write(0, 16, '去年销售量')
    worksheet.write(0, 17, '去年销售成本')
    worksheet.write(0, 18, '去年销售金额')
    worksheet.write(0, 19, '去年毛利额')
    for r in range(len(sql_result)):
        for c in range(len(sql_result[r])):
            if c in (0, 1):  # 第一、二列为日期格式
                worksheet.write(r + 1, c, sql_result[r][c], date_format)
            else:
                worksheet.write(r + 1, c, sql_result[r][c])

    workbook.close()


# 发送邮件
def send_email(v_date):
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
        smtp.sendmail('tigeryangjin@outlook.com', '12109471@qq.com', str(msg))  # 发送邮件
        smtp.quit()
        print('邮件发送成功！')
    except Exception as e:
        print(Exception, ":", e)


def yili_email(v_date):
    # 导出xlsx文件到磁盘
    export_excel_file(v_date)
    # 导出文件作为附件发送邮件
    send_email(v_date)


send_email('2016-06-05')
