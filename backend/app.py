import os
from flask import Flask, jsonify
app = Flask(__name__)

MESSAGE = os.getenv("MESSAGE", "")

@app.route('/', methods=['GET'])
def hello():
    return MESSAGE

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
