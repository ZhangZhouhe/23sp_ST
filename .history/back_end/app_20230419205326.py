# 导入 Flask
from flask import Flask, jsonify
from extension import db
app=Flask(__name__)
db.init_app(app)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__=='__main__':
    app.run(debug=True)