from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
class Health_active_shards(db.Model):
    date=db.Column(db.DateTime)
    cluster_name=db.Column(db.String(35))
    Health_active_shards=db.Column(db.Integer)
class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份 
@app.route('/')
def index():
    return 0
#def index():
#    cursor=db.cursor()
#    sql="SELECT date,health_active_shards FROM health_active_shards"
#    cursor.execute(sql)
#    shards=cursor.fetchall()
#    sql="SELECT date,health_status FROM health_status"
#    cursor.execute(sql)
#    status=cursor.fetchall()
#    return render_template('index.html', results=[shards,status])