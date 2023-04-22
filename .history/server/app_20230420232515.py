from flask import Flask,render_template
import pymysql
from markupsafe import escape
import os
db =pymysql.connect("localhost","root","huyang!153","fortest")
app=Flask(__name__)
@app.route('/')
def index():
    cursor=db.cursor()
    sql="SELECT date,health_active_shards FROM health_active_shards"
    cursor.execute(sql)
    results=cursor.fetchall()
    return render_template('index.html', results=results)