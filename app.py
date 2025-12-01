import os
from uuid import uuid4
from keras.utils import load_img, img_to_array
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['Alternaria',
           'Healthy',
           'Leaf Hopper and Jassids',
           'Leaf Miner',
           'Not Groundnut',
           'Rust',
           'Tobacco Caterpillar',
           'late and early leaf spot']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        # import tensorflow as tf
        import numpy as np
        # from keras.preprocessing import image

        from keras.models import load_model
        new_model = load_model('final.h5')
        new_model.summary()
        test_image = load_img('images\\' + filename, target_size=(256, 256))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = new_model.predict(test_image)
        predicted_class = classes[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)
    return render_template("template.html", image_name=filename, text=predicted_class, con = confidence)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__ == "__main__":
    app.run(debug=False)
