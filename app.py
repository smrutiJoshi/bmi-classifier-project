import os
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)
MODEL_PATH = os.path.join('models', 'bmi_category_cnn_sequential.h5')
IMG_SIZE = (224, 224)
CATEGORIES = ['Normal weight', 'Obesity', 'Overweight', 'Underweight']

# Load model once at startup
model = load_model(MODEL_PATH)

def predict_category(image_path):
    img = load_img(image_path, target_size=IMG_SIZE)
    img_arr = img_to_array(img) / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    pred = model.predict(img_arr)
    class_idx = np.argmax(pred)
    return CATEGORIES[class_idx]

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', prediction='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', prediction='No selected file')
        if file:
            os.makedirs('uploads', exist_ok=True)
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            category = predict_category(filepath)
            # Pass the filename to the template for display
            return render_template('index.html', prediction=f'Predicted BMI Category: {category}', image_url=url_for('uploaded_file', filename=file.filename))
    return render_template('index.html', prediction=None, image_url=None)


# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)
