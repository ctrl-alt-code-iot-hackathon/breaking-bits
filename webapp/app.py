from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

classifier = load_model("/Users/frankhart/Desktop/breaking-bits/webapp/static/model/malaria.h5")

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():

    if request.method == "POST":
        file = request.files['image']
        file_name = secure_filename(file.filename)
        file_loc = "/Users/frankhart/Desktop/breaking-bits/webapp/static/images/" + file_name
        file.save(file_loc)

        test_image = image.load_img(file_loc, target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)

        if result[0][0] >= 0.5:
          prediction = "Uninfected"
        else:
          prediction = "Parasitized"

        return jsonify({"prediction": prediction})

    return render_template("index.html")
