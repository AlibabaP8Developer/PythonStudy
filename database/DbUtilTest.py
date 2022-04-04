import DbUtil

insert_sql = "insert into user(id, username) values('2', '2')"
delete_sql = "delete from user where id = '1'"
result = DbUtil.connect_db_insert_update_delete(delete_sql, "commit")
print(result)
