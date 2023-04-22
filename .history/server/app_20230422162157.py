from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import click
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
#flask自定义命令
@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否删除后重建
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息
@app.route('/')
def index():
    shards=db.session.query(Health_active_shards.date,Health_active_shards.Health_active_shards).all()
    status=Health_status.query.all()
    return render_template('index.html',results=[shards,status])