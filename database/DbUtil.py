# 1.导包
import pymysql

# 定义数据库连接参数
host = "139.198.181.54"
port = 3306
user = "root"
password = "123456"
database = "leetcode"
charset = "utf8"


# 连接数据库
def connect_self(sql):
    # 2.创建连接对象
    conn = pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=password,
                           database=database,
                           charset=charset)
    # 3.获取游标,目的就是执行sql语句
    cursor = conn.cursor()
    # 4.执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭游标再关闭连接
    cursor.close()
    conn.close()
    return result

