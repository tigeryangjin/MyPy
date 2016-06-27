# Python3.5
# -*- coding: utf-8 -*-
# Author by YangJin

import cx_Oracle
import os
import xlsxwriter

# import smtplib
# import email.mime.multipart
# import email.mime.text
# import datetime

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码


def ra_batch_monitor():
    # ra日结执行时间导出到excel
    # Oracle查询SQL文件
    sql_file = open('D:\WORK\BBG\RMS-RA Data check\RA-UC4执行时间监控\Python_ra_batch_monitor.sql', 'r')
    sql_lines = sql_file.readlines()
    sql_text = ''
    for i in range(len(sql_lines)):
        sql_text += sql_lines[i].strip() + ' '
    # print(sql_text)
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
    datetime_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss', 'font_size': 9, 'font_name': '宋体'})
    time_format = workbook.add_format({'num_format': 'hh:mm:ss', 'font_size': 9, 'font_name': '宋体'})
    head_format = workbook.add_format({'bold': 1, 'font_size': 9, 'font_name': '宋体'})
    data_format = workbook.add_format({'font_size': 9, 'font_name': '宋体'})

    # 设置列宽度
    worksheet.set_column('A:A', 7)  # 定义A列宽度为80
    worksheet.set_column('B:B', 9)  # 定义A列宽度为80
    worksheet.set_column('C:C', 25)  # 定义A列宽度为80
    worksheet.set_column('D:D', 16)  # 定义A列宽度为80
    worksheet.set_column('E:E', 16)  # 定义A列宽度为80
    worksheet.set_column('F:F', 8)  # 定义A列宽度为80
    worksheet.set_column('G:G', 17)  # 定义A列宽度为80
    worksheet.set_column('H:H', 20)  # 定义A列宽度为80

    # 写入列名
    worksheet.write(0, 0, 'PHASE', head_format)
    worksheet.write(0, 1, 'DAYS', head_format)
    worksheet.write(0, 2, 'AH_NAME', head_format)
    worksheet.write(0, 3, 'START_TIME', head_format)
    worksheet.write(0, 4, 'END_TIME', head_format)
    worksheet.write(0, 5, 'RUN_TIME', head_format)
    worksheet.write(0, 6, 'MONTH_AVG_RUNTIME', head_format)
    worksheet.write(0, 7, 'STATUS', head_format)
    # 导出数据
    for row in range(len(sql_result)):
        for column in range(len(sql_result[row])):
            if column == 1:  # 第二列为日期格式
                worksheet.write(row + 1, column, sql_result[row][column], date_format)
            elif column in (3, 4):  # 开始时间，结束时间
                worksheet.write(row + 1, column, sql_result[row][column], datetime_format)
            elif column in (5, 6):  # 执行时间，月平均执行时间
                worksheet.write(row + 1, column, sql_result[row][column], time_format)
            else:
                worksheet.write(row + 1, column, sql_result[row][column], data_format)
    workbook.close()
    print('导出到xlsx文件成功！')

    # for i in range(len(sql_result)):
    #     print(sql_result[i])


def ra_batch_error():
    # ra日结报错信息
    pass


ra_batch_monitor()
