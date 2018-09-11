from flask import Flask, request, jsonify
from flask_cors import CORS
#from serve import get_model_api  # see part 1.
from predict import get_model_api

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
model_api = get_model_api()


# default route
@app.route('/')
def index():
    return "Index API"

@app.route('/predict', methods=['POST'])
def api():
    file = request.files['file'].read()
    output_data = model_api(file)
    response = jsonify({'text': output_data})
    return response
