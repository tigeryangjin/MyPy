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
    # Oracle查询SQL文件
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

    # 查询结果导出到excel
    workbook = xlsxwriter.Workbook('D:\WORK\BBG\RMS-RA Data check\RA-UC4执行时间监控\output.xlsx')
    # 创建
    worksheet = workbook.add_worksheet()

    # Add an Excel date format.
    date_format = workbook.add_format({'num_format': 'yyyy/mm/dd', 'font_size': 9, 'font_name': '宋体'})
    head_format = workbook.add_format({'bold': 1, 'font_size': 9, 'font_name': '宋体'})
    data_format = workbook.add_format({'font_size': 9, 'font_name': '宋体'})

    # 写入列名
    worksheet.write(0, 0, 'PHASE', head_format)
    worksheet.write(0, 1, 'DAYS', head_format)
    worksheet.write(0, 2, 'AH_NAME', head_format)
    worksheet.write(0, 3, 'START_TIME', head_format)
    worksheet.write(0, 4, 'END_TIME', head_format)
    worksheet.write(0, 5, 'RUN_TIME', head_format)
    worksheet.write(0, 6, 'MONTH_AVG_RUNTIME', head_format)
    worksheet.write(0, 6, 'STATUS', head_format)
    # 导出数据
    for row in range(len(sql_result)):
        for column in range(len(sql_result[row])):
            if column in (0, 1):  # 第一、二列为日期格式
                worksheet.write(row + 1, column, sql_result[row][column], date_format)

            else:
                worksheet.write(row + 1, column, sql_result[row][column], data_format)
    workbook.close()
    print('导出到xlsx文件成功！')

    # for i in range(len(sql_result)):
    #     print(sql_result[i])


ra_batch_monitor()
