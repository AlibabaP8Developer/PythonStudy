# 1.导包
import pymysql

# 定义数据库连接参数
host = "139.198.181.54"
port = 3306
user = "root"
password = "123456"
database = "leetcode"
charset = "utf8"


# 执行sql并查询所有
def connect_db_select_list(sql):
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


# 执行sql并查询一条
def connect_db_select_one(sql):
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
    result = cursor.fetchone()
    # 关闭游标再关闭连接
    cursor.close()
    conn.close()
    return result


# 执行sql查询指定条数
# size：要查询的数据条数
def connect_db_select_size(sql, size):
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
    result = cursor.fetchmany(size)
    # 关闭游标再关闭连接
    cursor.close()
    conn.close()
    return result


# 执行sql并查询所有
# sql：要执行的sql
# type：操作类型，commit提交，rollback回滚
def connect_db_insert_update_delete(sql, type):
    # 2.创建连接对象
    conn = pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=password,
                           database=database,
                           charset=charset)
    # 3.获取游标,目的就是执行sql语句
    cursor = conn.cursor()
    if type == "commit":
        try:
            # 4.执行sql语句
            # 对数据库完成添加、删除、修改操作，需要提交到数据库
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            # 对数据进行撤销
            e.with_traceback()
            conn.rollback()
        finally:
            # 关闭游标再关闭连接
            cursor.close()
            conn.close()
        return 1
    elif type == "rollback":
        try:
            conn.rollback()
            return 1
        finally:
            # 关闭游标再关闭连接
            cursor.close()
            conn.close()
            return -1
