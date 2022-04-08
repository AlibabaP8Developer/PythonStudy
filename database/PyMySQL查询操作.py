"""
py和mysql数据库交互
1.安装pymysql第三方包
    sudo pip3 install pymysql
    查看第三方包的信息：pip3 show pymysql、pip3 list
    第三方包存放路径：
        Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages

2.导入pymysql
    import pymysql
"""

# 1.导包
import pymysql

# 2.创建连接对象
"""
Connect = connect = Connection = connections.Connection
"""
conn = pymysql.connect(host="139.198.181.54",
                       port=3306,
                       user="root",
                       password="123456",
                       database="leetcode",
                       charset="utf8")

# 3.获取游标,目的就是执行sql语句
cursor = conn.cursor()
sql = "select * from user"

# 4.执行sql语句
cursor.execute(sql)

# 5.获取查询结果
# row = cursor.fetchone()
# print("row:", row)
# 获取所有查询结果
result = cursor.fetchall()
print("result:", result)

# 5.关闭游标再关闭连接
cursor.close()
conn.close()
