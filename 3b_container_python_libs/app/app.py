from flask import Flask, jsonify
import cv2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! <a href="/opencv-version">Check OpenCV version</a>'

@app.route('/opencv-version')
def opencv_version():
    return jsonify({'opencv_version': cv2.__version__})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
