# app.py
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Placeholder for disease detection function
def detect_disease(image_path):
    # Implement your disease detection logic here
    # You can use a pre-trained model or an external API

    # For simplicity, returning a placeholder result
    return "Leaf Spot", "Apply fungicide"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Create the 'uploads' folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    if 'image' not in request.files:
        return render_template('index.html')

    file = request.files['image']

    if file.filename == '':
        return render_template('index.html')

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        disease, solution = detect_disease(file_path)

        os.remove(file_path)

        return render_template('index.html', result=disease, solution=solution)

if __name__ == '__main__':
    app.run(debug=True)
