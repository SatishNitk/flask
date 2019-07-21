from flask import Flask,jsonify,request
from flask_restful import Api,Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)


client = MongoClient("mongodb://db:27017") # create connection
db = client.SentencesDatabase  # create dp
users = db['Users']  #create collection




def verifypw(username, password):
    hashed_pw = users.find({"Username":username})[0]['Password']

    if bcrypt.hashpw(password.encode("utf8"),hashed_pw) == hashed_pw:
        return True
    else:
        return False

def CountToken(username):
    token = users.find({"Username":username})[0]['Token']
    return token
    


class Register(Resource):
    def post(self):
        postData = request.get_json()
        username = postData['username']
        password = postData['password']


        hashed_pw = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())

        users.insert({
            "Username" :username,
            "Password" : hashed_pw,
            "Sentence" : "",
            "Token" : 6
            })
        retjson = {
          'status' : 200,
          "Msg" : "You successfully signup to the api"
        }
        return jsonify(retjson)


class Store(Resource):
    def post(self):
        postData = request.get_json()
        username = postData['username']
        password = postData['password']
        sentence = postData['sentence']
 
        correct_pw = verifypw(username,password)
        if not correct_pw:
            retjson = {
            'status' : 302
            }
            return jsonify(retjson)

        enough_token = CountToken(username)
        if enough_token <= 0:
            retjson = {
            "status": 302
            }
            return jsonify(retjson)

        users.update({
            "Username":username
            }, {
            "$set":{"Sentence":sentence,
                  "Token" : enough_token - 1
               }
            })
        retjson = {
        "status" : 200,
        "msg" :" sentence ssave successfully"
        }
        return jsonify(retjson)

class getResource(Resource):
    def post(self):
        postData = request.get_json()
        username = postData['username']
        password = postData['password']

        correct_pw = verifypw(username,password)
        if not correct_pw:
            retjson = {
            'status' : 302
            }
            return jsonify(retjson)
        sentence = users.find({"Username":username})[0]['Sentence']
        retjson  = {
        "status_code" : 200,
        "sentence" : sentence
        }
        return jsonify(retjson)





@app.route('/')
def hello_world():
    return "Hello World from spp2`"







api.add_resource(Register, '/register')
api.add_resource(Store,'/store')
api.add_resource(getResource,'/get')







if __name__ == "__main__":
    app.run(host= '0.0.0.0')



"""
to run..
......

export FLASK_APP=second_session_rest_api.py
flsk run

"""
