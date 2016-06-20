def query1():
    import cx_Oracle

    item_list = "900001119"

    try:
        rms = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
        cursor = rms.cursor()
        cursor.execute("select * from item_master t where t.item = :i ", i=item_list)
        sql_result = cursor.fetchall()
        cursor.close()
        rms.close()
        print('SQL查询完成！')
    except Exception as e:
        print(Exception, ":", e)

    print(sql_result)


def query2():
    import cx_Oracle

    item_list = "(900001119,900001126)"
    print(item_list)

    try:
        rms = cx_Oracle.connect('rms', 'Rms12345', 'dm03-scan.bbgretek.com.cn:1521/rmsdb')
        cursor = rms.cursor()
        cursor.execute("select * from item_master t where t.item in  :i  ", i=item_list)
        sql_result = cursor.fetchall()
        cursor.close()
        rms.close()
        print('SQL查询完成！')
    except Exception as e:
        print(Exception, ":", e)

    print(sql_result)


query1()
query2()
