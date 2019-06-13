from flask import Flask, request, jsonify, send_file

import firebase_driver

app = application = Flask(__name__)


@app.route('/upload/<string:source>', methods=['POST'])
def upload(source):
    file = request.files['picture']
    firebase_driver.upload(file, source)
    return jsonify(''), 200


@app.route('/<string:source>', methods=['GET'])
def get(source):
    file_path = firebase_driver.get(source)
    return send_file(file_path), 200


if __name__ == '__main__':
    app.run(port=8000, debug=True)
