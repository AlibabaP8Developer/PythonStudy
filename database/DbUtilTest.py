import DbUtil

result = DbUtil.connect_self("select * from user where sex=1")
print(result)
