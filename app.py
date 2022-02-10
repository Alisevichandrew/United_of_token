from functools import wraps
from xmlrpc.client import WRAPPERS
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
#(Flask, jsonify, request, session, make_response, render_template - are for tokens)

import uuid
import pymongo
import jwt #for token
import datetime #for token
from passlib.hash import pbkdf2_sha256
from user.models import User



app = Flask(__name__)

app.config['SECRET_KEY'] = b'Z\x864\x94\x8a\xf2\x92\x1c\xb1&\xda\xff\x84\xdfc\x8c'
#generation by command in terminal:> python -c 'import os; print(os.urandom(16))'

#Data base e.g "MongoDB Compass"
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system #this name we will see in e.g. "MongoDB Compass"

#Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
     return f(*args, **kwargs)
    else:
     return redirect('/')

  return wrap

# Create the user object
class User:
  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200


  def signup(self):
    print(request.form) #open 'User data' in terminal by VS code

# Personal data of user
    user = {
      "_id": uuid.uuid4().hex,
      "token": request.args.get('token'), #check this
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }
    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Chesk for existing email address
    if db.users.find_one({ "email": user['email'] }):
        return jsonify({"error": "Email address already in use"}), 400

    if db.users.insert_one(user): 
        return self.start_session(user)
        

    return jsonify({ "error": "Signup failed" }), 400

  def signout(self):
    session.clear()
    return redirect('/')

 
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)

    return jsonify({"error": "Invalid login credentials" }), 401 


#Token's create

def check_for_token(func):
  @wraps(func)
  def wrapped(*args, **kwargs):
    token = request.args.get('token')
    if not token:
      return jsonify({'messege': 'Missing token'}), 403
    try:
      data = jwt.decode(token, app.config['SECRET_KEY'])
    except:
      return jsonify({'message': 'Invalid token'}), 403
    return func(*args, **kwargs)
  return wrapped


#Token's route
@app.route('/token')
def index():
  if not session.get('logged_in'):
    return render_template('dashboard.html') #check it
  else:
    return 'Currently logged in'

@app.route('/public')
def public():
  return 'Anyone can view this'

@app.route('/auth')
@check_for_token
def authorized():
    return 'This is only viewable with a token'

#Login page of token 
@app.route('/login', methods=['POST'])
def login():
  if request.form['name'] and request.form['password'] == 'password':
    session['logged_in'] = True
    token = jwt.encode({
      'user': request.form['name'],
      'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    },
    app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('utf-8')})
  else:
    return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Login Failed "'})
    


# Routes of 'app.py'
from user import routes

@app.route('/')  
def base():
    return render_template('home.html')

@app.route('/base/') 
def home():
    return render_template('base.html')

@app.route('/dashboard/') 
@login_required
def dashboard():
    return render_template('dashboard.html')

# imitation of "file" routes.py
@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/Login', methods=['POST'])
def login():
    return User().login()


app.run(port=5000)

if __name__ == "__main__": 
  app.run(debug=True)
