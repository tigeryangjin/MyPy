import cx_Oracle
  
conn = cx_Oracle.connect('radm/RADM@ra-scan.bbgretek.com.cn/radb')
cursor = conn.cursor ()  
cursor.execute ("select * from dual")  
row = cursor.fetchone ()  
print(row[0])
  
cursor.close ()  
conn.close () 