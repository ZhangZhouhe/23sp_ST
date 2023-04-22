from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
class Health_active_shards(db.Model):
    date=db.Column(db.DateTime,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    Health_active_shards=db.Column(db.Integer)
class Health_status(db.Model):
    date=db.Column(db.DateTime,primary_key=True)
    cluster_name=db.Column(db.String(35),primary_key=True)
    Health_status=db.Column(db.Integer)

@app.route('/')
def index():
    
#def index():
#    cursor=db.cursor()
#    sql="SELECT date,health_active_shards FROM health_active_shards"
#    cursor.execute(sql)
#    shards=cursor.fetchall()
#    sql="SELECT date,health_status FROM health_status"
#    cursor.execute(sql)
#    status=cursor.fetchall()
#    return render_template('index.html', results=[shards,status])