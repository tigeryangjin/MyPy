# Python3.5
# Author yangjin
# 2016-06-03
# 分成二个步骤：
# 步骤一：通过yangjin.sql生成的sql语句保存到指定目录
# 步骤二：分割步骤一生成的sql语句，并生成对应的批处理脚本


import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文编码

# oracle连接参数
# conn = cx_Oracle.connect('RADM', 'RADM', 'ra-scan.bbgretek.com.cn:1521/radb') #RADM
v_user = 'rms'
v_password = 'Rms12345'
v_description = 'dm03-scan.bbgretek.com.cn:1521/rmsdb'

# 参数配置
v_top_sql_file = 'copy_ALL.sql'  # 查询结果保存文件
v_top_bat_file = 'all_start_bat.bat'  # 生成的总批处理文件
v_path = 'G:\Documents\MyPy\MyPy\Text_segmentation\output\\'  # 存放目录
v_sql_path = 'G:\Documents\MyPy\MyPy\Text_segmentation\yangjin2.sql'
v_row_num = 10  # 每个分割文件的行数
v_spool_begin = "spool d:\cp_to_zb\log\\"
v_spool_end = 'spool off;'
v_sub_file_name_head = 'copy'  # 生成分割文件名Head

sql_result = []  # sql查询结果作为全局变量


# sql查询结果保存到文件
def sql_query_to_file():
    # 如果目录不存在则创建目录
    if os.path.exists(v_path):
        pass
    else:
        os.makedirs(v_path)
    # yangjin.sql文件读入sql_text字符串
    sql_text = ''
    sql_file = open(v_sql_path, 'r', encoding="utf8")
    sql_segment = sql_file.readlines()
    for i in range(len(sql_segment)):
        sql_text += sql_segment[i].strip() + ' '

    # 连接配置
    conn = cx_Oracle.connect(v_user, v_password, v_description)
    cursor = conn.cursor()
    cursor.execute(sql_text)
    global sql_result
    sql_result = cursor.fetchall()
    cursor.close()
    conn.close()

    # 保存结果到copy_ALL.sql文件
    all_file = open(v_path + v_top_sql_file, 'w')
    for i in range(len(sql_result)):
        all_file.writelines(sql_result[i][0])
    all_file.close()


# 开始分割文件并生成批处理文件
def generate_file_all():
    # 生成分割文件
    seg_file = open(v_path + v_top_sql_file, 'r')
    tmp_data = seg_file.readlines()
    for fileid in range(len(tmp_data) // v_row_num + 1):
        new_file = open(v_path + v_sub_file_name_head + str(fileid + 1) + '.sql', 'w')  # 生成一个新文件
        new_file.writelines(v_spool_begin + v_sub_file_name_head + str(fileid + 1) + '.log' + '\n')
        row_id = fileid * v_row_num + 1  # 开始读取行号
        # 开始插入指定的行数
        for i in range(row_id, row_id + v_row_num):
            if i >= len(tmp_data):
                pass
            else:
                new_file.writelines(tmp_data[i])
        new_file.writelines(v_spool_end)
        new_file.close()

    # 生成bat批处理文件
    # sqlplus /nolog @copy_1.sql
    seg_file = open(v_path + v_top_sql_file, 'r')
    tmp_data = seg_file.readlines()
    for fileid in range(len(tmp_data) // v_row_num + 1):
        bat_file = open(v_path + v_sub_file_name_head + str(fileid + 1) + '.bat', 'w')
        bat_file.writelines('sqlplus /nolog @' + v_sub_file_name_head + str(fileid + 1) + '.sql')
        bat_file.close()

    # 生成总的bat批处理文件
    total_bat_file = open(v_path + v_top_bat_file, 'w')
    total_bat_file.writelines('@echo off\n')
    total_bat_file.writelines('\n')
    total_bat_file.writelines('REM --------------------------------------------------\n')
    total_bat_file.writelines('REM 启动所有bat\n')
    total_bat_file.writelines('REM --------------------------------------------------\n')
    total_bat_file.writelines('@echo #正在启动......\n')
    total_bat_file.writelines('\n')
    total_bat_file.writelines('d:\n')
    total_bat_file.writelines('\n')
    for i in range(len(tmp_data) // v_row_num + 1):
        total_bat_file.writelines('cd ' + v_path + '\n')
        total_bat_file.writelines(
            'start "' + v_sub_file_name_head + str(i + 1) + '.bat"' + v_sub_file_name_head + str(i + 1) + '.bat\n')
        total_bat_file.writelines('\n')
    total_bat_file.writelines('exit;\n')
    total_bat_file.close()


def generate_file_area():
    # 生成分割文件
    seg_file = open(v_path + v_top_sql_file, 'r')
    tmp_data = seg_file.readlines()
    print(tmp_data)
    print(sql_result)
    pass


sql_query_to_file()
# generate_file_all()
generate_file_area()
