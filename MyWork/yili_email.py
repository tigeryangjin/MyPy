# Python3.5
# -*- coding: utf-8 -*-

import cx_Oracle
import os
import csv
from openpyxl import Workbook  # 读取excel
from openpyxl import load_workbook  # 写入excel

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码

# sys.setdefaultencoding('utf8')

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

# 数据导出到excel文件
path = 'D:\WORK\BBG\JOB\伊利\表格\ '
path.strip()
# excel_file = open(path + 'yj001.xls', 'w')
# for i in range(len(sql_result)):
#     excel_file.writelines(str(sql_result[i])+'\n')
# excel_file.close()

with open(path + "XXX.xlsx", "w", newline="") as datacsv:
    # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
    for i in range(len(sql_result)):
        csvwriter.writerow(str(sql_result[i])+'\n')
