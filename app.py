from flask import Flask
from flask import request
from flask_restful import reqparse
from chatbotmodel import ChatModel
from flask import jsonify
from flask_cors import cross_origin

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

chatmodel = ChatModel()

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    request_data = request.get_json(silent=True)
    response = jsonify(chatmodel.evaluate(request_data['sentence']))
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
