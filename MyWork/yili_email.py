# Python3.5
# -*- coding: utf-8 -*-

import cx_Oracle
import os
import xlsxwriter
import time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码

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
v_curr_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
v_file_name = 'YM_' + v_curr_time + '.xlsx '
print(v_file_name)
workbook = xlsxwriter.Workbook(v_file_name)
# 创建
worksheet = workbook.add_worksheet()
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
        worksheet.write(r + 1, c, sql_result[r][c])

workbook.close()