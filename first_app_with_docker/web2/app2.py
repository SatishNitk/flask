from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return "Hello World from spp2`"




@app.route('/add_two_number/',methods=['POST'])
def add_two_numer():
    json_dict = request.get_json()
    if "x" not in json_dict or "y" not in json_dict:
        return "ERROR",305
    x= json_dict['x']
    y= json_dict['y']
    z = x + y
    retjson = {
    'z':z
    }
    return jsonify(retjson),200

def checkpostedData(postedData, function_name):
    if function_name == 'add' or function_name == "subtract" or function_name == 'multiply':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    elif(function_name == 'divide'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif(int(postedData['y']) == 0):
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostedData(postData,'add')
        if int(status_code) != 200:
            res = {
            'msg' :" ERROR occured",
            "status_code" : status_code
            }
            return jsonify(res)

        x = postData['x']
        y = postData['y']
        z = int(x) + int(y)
        retMap = {
           "sum":z,
            "status code": 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostedData(postData, "subtract")
        if status_code != 200:
            retMap = {
            'msg' : " ERROR occured in subtract",
            'status_code' : status_code
            }
            return jsonify(retMap)

        z = int(postData['x']) - int(postData['y'])
        retMap = {
        'res' :z,
        "status_code" : 200
        }    
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostedData(postData, "multiply")
        if status_code != 200:
            retMap = {
            "msg" : "ERROR occured",
            'status_code': status_code
            }
            return jsonify(retMap)
        z = int(postData['x']) * int(postData['y'])
        retMap = {
        "res" : z,
        "status_code" : 200
        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        postData = request.get_json()
        status_code = checkpostedData(postData,'divide')
        if status_code != 200:
            retMap = {
            'msg': "ERROR occured",
            "status_code" :status_code
            }
            return jsonify(retMap)
        z = int(postData['x']) / int(postData['y'])
        retMap = {
        'res':z,
        "status_code" : 200
        }
        return jsonify(retMap)


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')




if __name__ == "__main__":
    app.run(host= '0.0.0.0')



"""
to run..
......

export FLASK_APP=second_session_rest_api.py
flsk run

"""
