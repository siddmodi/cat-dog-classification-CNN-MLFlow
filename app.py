from flask import Flask, request, jsonify, render_template
import os
import tensorflow
# from flask_cors import CORS, cross_origin
from src.utils.img_preprocess import decodeImage , encodeImageIntoBase64 
from src.stage_05_prediction import dogcat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
# CORS(app)

#@cross_origin()
class app1:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)

@app.route("/", methods=['GET'])
# @cross_origin()
def home():
    return render_template('index.html')
    
@app.route("/predict", methods=['POST'])
# @cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, app1().filename)
    result = app1().classifier.predictiondogcat()
    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = app1()
    #app.run(host='0.0.0.0', port=port)
    app.run()
    # app.run(host='0.0.0.0', port=8000, debug=True)
