作者：小凋
链接：https://www.zhihu.com/question/574760299/answer/2987058868
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 导入 Flask
from flask import Flask, jsonify
   # 导入 CORS
from flask_cors import CORS

# 创建一个 Flask 应用实例
app = Flask(__name__)
# 并允许来自所有域的请求
CORS(app)

# 定义一个简单的路由
@app.route('/api/data', methods=['GET'])
def get_data():
    # 创建一个字典作为模拟数据
    data = {
        "message": "Hello from Flask!",
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }
    # 将字典转为 JSON 并返回
    return jsonify(data)

# 如果作为主程序运行，启动应用
if __name__ == '__main__':
    app.run(debug=True)
