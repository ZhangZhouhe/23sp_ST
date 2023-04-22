from flask import Flask,render_template
import pymysql
db =pymysql.connect(host="localhost",user="root",password="huyang!153",database="data")
app=Flask(__name__)
@app.route('/')
def index():
    cursor=db.cursor()
    sql="SELECT date,health_active_shards FROM health_active_shards"
    cursor.execute(sql)
    shards=cursor.fetchall()
    sql="SELECT date,health_status FROM health_status"
    cursor.execute(sql)
    status=cursor.fetchall()
    
    return render_template('index.html', results=[shards,status])

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码