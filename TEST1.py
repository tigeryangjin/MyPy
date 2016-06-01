import cx_Oracle

# conn = cx_Oracle.connect('rcx_Oracleadm/RADM@ra-scan.bbgretek.com.cn/radb')
# conn = cx_Oracle.conn('rman/rman@192.168.2.210:1521/rman')
conn = cx_Oracle.connect('rman', 'rman', '192.168.2.210:1521/rman')
cursor = conn.cursor()
cursor.execute("")
row = cursor.fetchone()
print(row[0])

cursor.close()
conn.close()
