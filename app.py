from flask import Flask, render_template ,session, redirect, url_for ,request
from blueprints.authentication import auth 
from lib.apiKeyClass import APIKey
from lib.groupClass import Group
from blueprints.dialog import dialog
from blueprints.apikeys import api
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.secret_key= os.getenv('SECRET_KEY')
# print("Secret Key Loaded:", app.secret_key)  # Debugging line to confirm secret key is loaded
app.register_blueprint(auth)
app.register_blueprint(dialog)
app.register_blueprint(api)

@app.route("/")
def home():
    return "Welcome to Zyneriq! Please visit /dashboard to access your dashboard."

@app.before_request
def before_request():
    if session.get('type') == 'web':
        return 
    auth_heder = request.headers.get('Authorization')
   
    if auth_heder:
        try:
            api_key = auth_heder.split(" ")[1]  
            api_key_obj = APIKey(api_key)
            if api_key_obj and api_key_obj.is_valid():
                session['authenticated'] = True
                session['username'] = api_key_obj.collection.username
                session['type'] = 'api'
            else:
                session.clear()
        except Exception as e:
            session.clear() 
    else:
        session.clear()

@app.route("/dashboard")
def dashboard(): 
    
    if not session.get('authenticated'):
        print(session)  # Debugging line to check session contents
        return redirect(url_for('login'))
    else:
        return render_template("dashboard.html",session=session,username=session.get('username'))   
@app.route("/apikey")
def apikey():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    api_keys = APIKey.get_api_key_info()
    groups = Group.get_groups()
    
    return render_template("apikey.html",session=session,api_keys=api_keys,groups=groups)
@app.route("/profile")
def profile():
    return render_template("profile.html")  

@app.route("/devicetest")
def billing():
    if session.get('authenticated'):
        return 'Hello, this is a test endpoint for device information!' 
    else:
        return 'session not authenticated'
@app.route("/login")
def login():
    return render_template("login.html")    
@app.route("/signup")
def signup():
    return render_template("signup.html")
if __name__ == "__main__":
    app.run(debug=True)