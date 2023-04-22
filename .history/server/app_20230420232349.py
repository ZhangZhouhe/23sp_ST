from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from markupsafe import escape
import os
app=Flask(__name__)
db =pymysql.connect("localhost","root","huyang!153","fortest")
@app.route('/')
def index():
    cursor=db.cursor()
    sql="SELECT date,health_active_shards FROM health_active_shards"
    cursor.execute(sql)
    results=cursor.fetchall()
    return render_template('index.html', results=results)