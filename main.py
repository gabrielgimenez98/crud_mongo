from flask import Flask, request, json, Response
from mongo import MongoAPI
from settings import *

app = Flask(__name__)
mongo_db = MongoAPI()

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/mongodb', methods=['GET'])
def mongo_read():
    response = mongo_db.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')



@app.route('/mongodb', methods=['POST'])
def mongo_write():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = mongo_db.write(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/mongodb', methods=['PUT'])
def mongo_update():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = mongo_db.update(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')



@app.route('/mongodb', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    response = mongo_db.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
  
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')