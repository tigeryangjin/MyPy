# import os

file_name = 'copy_ALL.sql'  # 分割文件名
row_num = 10  # 分割行数
row_head = 'copy from'
row_head_length = len(row_head)
spool_first = "spool d:\cp_to_zb\log\ "
spool_first = spool_first.strip()
spool_last = 'spool off;'
file = open(file_name, 'r')
source_data = file.readlines()
output_file_name = 'copy'  # 生成文件名
output_file_id = 1
count = 0
# 中间临时文件处理，执行完成后删除
tmp_file = open('copy_tmp.sql', 'w')  # 生成一个新文件
for i in range(len(source_data)):
    if source_data[i][0:row_head_length] == row_head:
        tmp_file.writelines(source_data[i])
        count += 1
        if count / row_num == count // row_num:
            output_file_id += 1
tmp_file.close()

# 生成分割文件
tmp_file = open('copy_tmp.sql', 'r')
tmp_data = tmp_file.readlines()
for fileid in range(len(tmp_data) // 10 + 1):
    new_file = open(output_file_name + str(fileid + 1) + '.sql', 'w')  # 生成一个新文件
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

# 删除临时文件
# os.remove('copy_tmp.sql')
