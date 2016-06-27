import pymssql


# 上班考勤打卡
class MSSQL:
    """
    对pymssql的简单封装

    """

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def main():
    # ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    # #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    # ms.ExecNonQuery("insert into WeiBoUser values('2','3')")
    # 四楼:1911300460207
    # 三楼:1911300460094

    try:
        ms = MSSQL(host="192.168.2.228", user="sa", pwd="123", db="zktime8")
        delRec = ms.ExecNonQuery(
            "DELETE zktime8.dbo.CHECKINOUT   WHERE PIN='0006320835' AND CONVERT(varchar(100),CHECKTIME,112)=CONVERT(varchar(100), GETDATE(), 112);")
        insertRec1 = ms.ExecNonQuery(
            "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'08:00','08:25'),CONVERT(char(8),getdate(),112) + ' 08:00'),255,2,1911300460207,'0006320835');")
        insertRec2 = ms.ExecNonQuery(
            "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'12:00','12:10'),CONVERT(char(8),getdate(),112) + ' 12:00'),255,2,1911300460207,'0006320835');")
        insertRec3 = ms.ExecNonQuery(
            "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'12:30','12:40'),CONVERT(char(8),getdate(),112) + ' 12:30'),255,2,1911300460207,'0006320835');")
        insertRec4 = ms.ExecNonQuery(
            "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'17:30','18:00'),CONVERT(char(8),getdate(),112) + ' 17:30'),255,2,1911300460207,'0006320835');")
        query = ms.ExecQuery(
            "SELECT CHECKINOUT.checktime FROM zktime8.dbo.CHECKINOUT CHECKINOUT WHERE (CHECKINOUT.pin='0006320835') AND (CONVERT(CHAR(8),CHECKTIME,112)=CONVERT(CHAR(8),GETDATE(),112)) ORDER BY CHECKINOUT.checktime")
        print('Success!')
        for i in range(len(query)):
            print(query[i])
        input()
    except Exception as e:
        print(Exception, ":", e)
        input()

    # try:
    #     ms = MSSQL(host="192.168.2.228", user="sa", pwd="123", db="zktime8")
    #     delRec = ms.ExecNonQuery(
    #         "DELETE zktime8.dbo.CHECKINOUT   WHERE PIN='0001990676' AND CONVERT(varchar(100),CHECKTIME,112)=CONVERT(varchar(100), GETDATE(), 112);")
    #     insertRec1 = ms.ExecNonQuery(
    #         "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'08:00','08:25'),CONVERT(char(8),getdate(),112) + ' 08:00'),255,2,1911300460207,'0001990676');")
    #     insertRec2 = ms.ExecNonQuery(
    #         "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'12:00','12:10'),CONVERT(char(8),getdate(),112) + ' 12:00'),255,2,1911300460207,'0001990676');")
    #     insertRec3 = ms.ExecNonQuery(
    #         "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'12:30','12:40'),CONVERT(char(8),getdate(),112) + ' 12:30'),255,2,1911300460207,'0001990676');")
    #     insertRec4 = ms.ExecNonQuery(
    #         "INSERT INTO zktime8.dbo.CHECKINOUT(CHECKTIME,CHECKTYPE,VERIFYCODE,SN_NAME,PIN) VALUES(DATEADD(second,ABS(CHECKSUM(NEWID())) % DATEDIFF(second,'17:30','18:00'),CONVERT(char(8),getdate(),112) + ' 17:30'),255,2,1911300460207,'0001990676');")
    #     query = ms.ExecQuery(
    #         "SELECT CHECKINOUT.checktime FROM zktime8.dbo.CHECKINOUT CHECKINOUT WHERE (CHECKINOUT.pin='0001990676') AND (CONVERT(CHAR(8),CHECKTIME,112)=CONVERT(CHAR(8),GETDATE(),112)) ORDER BY CHECKINOUT.checktime")
    #     print('Success!')
    #     for i in range(len(query)):
    #         print(query[i])
    #     input()
    # except Exception as e:
    #     print(Exception, ":", e)
    #     input()


if __name__ == '__main__':
    main()
