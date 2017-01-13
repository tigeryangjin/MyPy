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