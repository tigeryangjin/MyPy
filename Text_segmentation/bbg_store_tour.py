# Python3.5

import cx_Oracle
import os

# Oracle中执行yangjin.sql文件，最后生成分割文件
file_name = 'copy_ALL.sql'  # 生成的总文件名
path = 'G:\Documents\MyPy\MyPy\Text_segmentation\output\ '  # 存放目录
path = path.strip()
# 如果目录不存在则创建目录
if os.path.exists(path):
    pass
else:
    os.makedirs(path)
row_num = 10  # 每个分割文件的行数
row_head = 'copy from'
row_head_length = len(row_head)
spool_first = "spool d:\cp_to_zb\log\ "
spool_first = spool_first.strip()
spool_last = 'spool off;'
output_file_name = 'copy'  # 生成文件名
output_file_id = 1
count = 0

# sql执行语句变量
# sql_text_sub = ("using select * from dpm")

# yangjin.sql文件读入sql_text字符串
sql_text = ''
sql_file = open('yangjin.sql', 'r')
sql_segment = sql_file.readlines()
for i in range(len(sql_segment)):
    sql_text += sql_segment[i].strip() + ' '

# 连接配置
# conn = cx_Oracle.connect('rman', 'rman', '192.168.2.210:1521/rman')
conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')  # RMS
# conn = cx_Oracle.connect('RADM', 'RADM', 'ra-scan.bbgretek.com.cn:1521/radb') #RADM
cursor = conn.cursor()
cursor.execute(sql_text)
sql_result = cursor.fetchall()
cursor.close()
conn.close()

# 保存结果到copy_ALL.sql文件
all_file = open(path + file_name, 'w')
for i in range(len(sql_result)):
    all_file.writelines(sql_result[i])
all_file.close()

# 开始分割
# 生成分割文件
seg_file = open(path + 'copy_ALL.sql', 'r')
tmp_data = seg_file.readlines()
for fileid in range(len(tmp_data) // 10 + 1):
    new_file = open(path + output_file_name + str(fileid + 1) + '.sql', 'w')  # 生成一个新文件
    new_file.writelines(spool_first + output_file_name + str(fileid + 1) + '.log' + '\n')
    row_id = fileid * row_num + 1  # 开始读取行号
    # 开始插入指定的行数
    for i in range(row_id, row_id + row_num):
        if i >= len(tmp_data):
            pass
        else:
            new_file.writelines(tmp_data[i])
    new_file.writelines(spool_last)
    new_file.close()

# 生成bat批处理文件
# sqlplus /nolog @copy_1.sql
seg_file = open(path + 'copy_ALL.sql', 'r')
tmp_data = seg_file.readlines()
for fileid in range(len(tmp_data) // 10 + 1):
    bat_file = open(path + output_file_name + str(fileid + 1) + '.bat', 'w')
    bat_file.writelines('sqlplus /nolog @' + output_file_name + str(fileid + 1) + '.sql')
    bat_file.close()

# 生成总的bat批处理文件
total_bat_file = open(path + 'all_start_bat.bat', 'w')
total_bat_file.writelines('@echo off\n')
total_bat_file.writelines('\n')
total_bat_file.writelines('REM --------------------------------------------------\n')
total_bat_file.writelines('REM 启动所有bat\n')
total_bat_file.writelines('REM --------------------------------------------------\n')
total_bat_file.writelines('@echo #正在启动copy_1.bat-copy_25.bat......\n')
total_bat_file.writelines('\n')
total_bat_file.writelines('d:\n')
total_bat_file.writelines('\n')
for i in range(len(tmp_data) // 10 + 1):
    total_bat_file.writelines('cd D:\cp_to_zb\ \n')
    total_bat_file.writelines(
        'start "' + output_file_name + str(i + 1) + '.bat"' + output_file_name + str(i + 1) + '.bat\n')
    total_bat_file.writelines('\n')
total_bat_file.writelines('exit;\n')
total_bat_file.close()
