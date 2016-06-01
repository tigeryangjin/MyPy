import cx_Oracle

sql_file = open('yangjin.sql', 'r')
sql_seg = sql_file.readlines()
sql_text = ''
for i in range(len(sql_seg)):
    # print('"' + sql_seg[i].strip() + '" +')
    sql_text += sql_seg[i].strip() + ' '

# sql_text = ("SELECT * " +
#             "FROM ITEM_MASTER T " +
#             "WHERE T.ITEM LIKE '800%' " +
#             "AND T.ITEM_LEVEL = T.TRAN_LEVEL " +
#             "AND T.DEPT = 21 ")

print(sql_text)
print(type(sql_text))

# conn = cx_Oracle.connect('rcx_Oracleadm/RADM@ra-scan.bbgretek.com.cn/radb')
# conn = cx_Oracle.conn('rman/rman@192.168.2.210:1521/rman')
conn = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
cursor = conn.cursor()
cursor.execute(sql_text)
row = cursor.fetchall()
print(row[10])

cursor.close()
conn.close()
