from flask import Flask, request, jsonify,redirect,url_for
app = Flask(__name__)


# root call
@app.route('/')
def hello_world():
	return "Hello World"

# http://127.0.0.1:5000/bye
@app.route('/bye')
def bye():
	return "Bye is calling"

# http://127.0.0.1:5000/hello/satish
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# http://127.0.0.1:5000/blog/21
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

# http://127.0.0.1:5000/rev/21.232
@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# http://127.0.0.1:5000/json_data
@app.route('/json_data')
def json_data():
	json_data1 = {
	"name":"satish",
	"roll":33,
	"phone":["11111","2121212"]
	}
	return jsonify(json_data1)


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))



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




if __name__ == '__main__':
   app.run(host= '0.0.0.0')


"""
to run..
......

export FLASK_APP=first_session.py
flsk run

"""
