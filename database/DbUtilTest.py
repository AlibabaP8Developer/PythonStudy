import DbUtil

sql = "insert into user(id, username) values('1', '1')"
result = DbUtil.connect_db_insert_update_delete(sql, "commit")
print(result)
