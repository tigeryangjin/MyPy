import time
import xlsxwriter

v_curr_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
v_file_name = 'YM_' + v_curr_time + '.xlsx '
print(v_file_name)
workbook = xlsxwriter.Workbook(v_file_name)
# 创建
worksheet = workbook.add_worksheet()
# 写入列名
worksheet.write(0, 0, '销售日期')
worksheet.write(0, 1, '去年同期日期')