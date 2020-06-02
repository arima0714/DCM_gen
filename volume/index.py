from flask import *

import gensim
model = gensim.models.Word2Vec.load("model_dev.model")

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"language":"python"})

@app.route("/test")
def testx():
    return make_response(jsonify({"ruigigo":"ruigigo"}))

@app.route("/input/<input_string>")
def return_input_string(input_string):
    return make_response(jsonify({"input_string":input_string}))

