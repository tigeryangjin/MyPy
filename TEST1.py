import cx_Oracle

rms = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
cursor = rms.cursor()
cursor.execute('select sysdate from dual')
query_result = cursor.fetchall()
cursor.close()
rms.close()

print(query_result)
dir(cx_Oracle)