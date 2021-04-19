import pymysql
from pymysql.cursors import DictCursor


class Connection:
    def __init__(self):
        try:
            self.conn = pymysql.Connect(
                user='pengfan758258',
                password='Pf@7758258',
                host='rm-bp1nq96t1655pm4djmo.mysql.rds.aliyuncs.com',
                port=3306,
                database='my_test',
                charset='utf8'
            )
        except Exception as e:
            raise ValueError('mysql connect error: {}'.format(e))

    def __enter__(self):
        # DictCursor针对查询到的结果进行dict化
        self.cursor = self.conn.cursor(cursor=DictCursor)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()  # 回滚事务
            # 日志收集异常信息，上报给服务器
        else:
            # 关闭链接
            self.cursor.close()
            self.conn.close()

    def close(self):
        try:
            self.conn.close()
        except:
            pass
