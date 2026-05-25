from dotenv import load_dotenv
import pymysql
import os

load_dotenv()
# 连接数据库
conn = pymysql.connect(
     host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT")),
    charset=os.getenv("DB_CHARSET")
)

# 创建游标对象
cursor = conn.cursor()

sql_str = [
'use mydb;',
'select database();',
'select * from students;'
]
for item in sql_str:
    cursor.execute(item)

# result = cursor.fetchone()#从服务端获取数据。只取一行
#fetchone从服务端获取数据。只取一行
#fetchall从服务端获取数据，获取所有数据
#fetmany(n)从服务端获取数据，获取N条数据
result = cursor.fetchall()
print(f"{result}")

# 关闭连接
cursor.close()  #关闭游标
conn.close()    #关闭数据库