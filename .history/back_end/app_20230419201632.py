from flask import Flask, render_template,jsonify
import json

app=Flask(__name__)
@app.route('/test', methods=['GET'])
def test():
    return json.dumps('hello world!')

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080")
