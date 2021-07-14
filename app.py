import os
import cv2
from flask import Flask, request, render_template
from keras.models import load_model
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['DEBUG'] = True
model = load_model('/Users/prathiklolla/Documents/heroku-app/Brain-Tumor-Detection/')


def output_string(classification):
    if classification == 0:
        return 'This brain has a tumor'
    else:
        return 'This brain does not have a tumor'

@app.route('/')
def home():
    return render_template('home.html')

def predict(IMG_PATH, model):
    # Some preprocessing
    img_array = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array, (224, 224))
    new_array = np.array(new_array).reshape(-1, 224, 224, 3)

    prediction = model.predict(new_array) # this will be an array with one element
    return float(prediction[0])
@app.route('/submit', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        render_template('home.html')
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['mri']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'static/uploads', secure_filename(f.filename))
        f.save(file_path)
        local_file_path = '/static/uploads/' + f.filename;
        prediction = predict(file_path, model)
        classification = ""
        if prediction > 0.60:
            classification = "This brain most likely has a tumor!!"
        else:
            classification = "This brain most likely doesn't have a tumor"

        return render_template('result.html', prediction=prediction, classification=classification, file=local_file_path)

if __name__ == '__main__':
    app.run()