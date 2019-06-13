import json

from flask import Flask, request, jsonify


app = application = Flask(__name__)

@app.route('/upload', methods=['POST'])
def uplaoad():
    data = json.loads(request.data)
    file = request.files['picture']
    print(data)
    print(file)

    return jsonify(True)

if __name__ == '__main__':
    app.run(port=8000, debug= True)