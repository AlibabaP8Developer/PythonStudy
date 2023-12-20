from pymysql import Connection

# 构建到mysql数据库连接
conn = Connection(host='139.198.181.54', port=3306, user='root', password='Dcp#7ujm')

# 数据库连接信息版本
print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()  # 获取到游标对象
conn.select_db('guigu-oa')  # 选择数据库
# 执行SQL
cursor.execute('select * from oa_process_template')

# 执行查询性质SQL
result: tuple = cursor.fetchall()
for row in result:
    print('查询结果：', row)

# 关闭连接
conn.close()
