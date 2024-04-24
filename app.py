import os
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
from flask import jsonify

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model paths
model_paths = {
    'model1': 'tumorfix.h5',
    'model2': 'inception.h5',
    'model3': 'vgg16.h5',
}

import os

# Load models
models = {model_name: tf.keras.models.load_model(model_path) for model_name, model_path in model_paths.items()}

labels = ['Glioma Tumor', 'No Tumor', 'Meningioma Tumor', 'Pituitary Tumor']

def model_predict(img_path, model_name):
    # Read the image
    img = Image.open(img_path)
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(opencvImage, (150, 150))
    img = img.reshape(1, 150, 150, 3)

    # Predict the class of the image
    prediction = models[model_name].predict(img)
    prediction_class = np.argmax(prediction, axis=1)[0]
    label = labels[prediction_class]

    # Get the confidence (probability) of the prediction
    confidence = np.max(prediction)

    # Convert confidence to percentage
    confidence_percent = round(confidence * 100, 2)

    return label, confidence_percent


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        model_name = request.form['model']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction using the selected model
        result, confidence = model_predict(file_path, model_name)

        # Convert the result and confidence to JSON format
        response = {'prediction': result, 'confidence': confidence}
        return jsonify(response)  # Use jsonify to convert response to JSON
    return None
    
# Route untuk halaman Tujuan Proyek
@app.route('/tujuan')
def tujuan():
    return render_template('tujuan.html')

# Route untuk halaman Penjelasan Tumor Otak
@app.route('/penjelasan')
def penjelasan():
    return render_template('penjelasan.html')

@app.route('/hasil_akurasi')
def hasil_akurasi():
    return render_template('hasil_akurasi.html')

if __name__ == '__main__':
    app.run(debug=False)
