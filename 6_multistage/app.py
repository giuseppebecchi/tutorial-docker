from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for
import os
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/app/uploads'
OUTPUT_FOLDER = '/app/outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/convert', methods=['POST'])
def convert_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.lower().endswith('.jpg'):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_filename = filename.rsplit('.', 1)[0] + '.png'
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

        file.save(input_path)

        # Convert image using OpenCV
        image = cv2.imread(input_path)
        cv2.imwrite(output_path, image)

        return redirect(url_for('download_form', filename=output_filename))

    return jsonify({'error': 'Invalid file type'}), 400


@app.route('/download/<filename>')
def download_form(filename):
    return render_template('download.html', filename=filename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
