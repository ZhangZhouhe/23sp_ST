from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/data')
def data():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run()