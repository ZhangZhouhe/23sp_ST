# 导入 Flask
from flask import Flask, jsonify
from extension import db
app=Flask(__name__)
db.init_app(app)

