from flask import *

import gensim
model = gensim.models.Word2Vec.load("model_dev.model")

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return jsonify({"language":"python"})

@app.route("/test")
def testx():
    return make_response(jsonify({"ruigigo":"ruigigo"}))

@app.route("/input/<input_string>")
def return_input_string(input_string):
    return make_response(jsonify({"入力文字列":input_string}))

@app.route("/most_similar/<input_string>")
def return_most_somilar(input_string):
    result = model.wv.most_similar(input_string)
    return_data = jsonify({"1":result[0][0], "2":result[1][0], "3":result[2][0]})
    return make_response(return_data)

