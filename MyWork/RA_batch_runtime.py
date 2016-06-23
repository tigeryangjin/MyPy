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


def ra_batch_monitor():
    # Oracle查询SQL
    sql_file = open('D:\WORK\BBG\RMS-RA Data check\RA-UC4执行时间监控\Python_ra_batch_monitor.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '
    print(sql_text)
    # 数据库连接信息
    try:
        conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
        cursor = conn.cursor()
        cursor.execute(sql_text)  # 执行查询
        sql_result = cursor.fetchall()
        cursor.close()
        conn.close()
        print('SQL查询完成！')
    except Exception as e:
        print(Exception, ":", e)
    print(type(sql_result))


ra_batch_monitor()
