import pymysql
#打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="huyang!153",database="data")
#使用cursor()方法获取操作游标 
cursor = db.cursor()
#sql语句
sql = "select * from health_active_shards"
try:
    #执行sql语句
    cursor.execute(sql)
    #查询中的一个操作，获取所有记录
    result = cursor.fetchall()
    #打印表数据
    for row in result:
        id = row[0]
        name = row[1]
        print(id,name)
except:
    print("Error!")
#关闭数据库
db.close()
