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