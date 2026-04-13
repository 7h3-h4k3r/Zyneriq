from flask import Flask, render_template ,session, redirect, url_for ,request
from blueprints.authentication import auth 
from lib.apiKeyClass import APIKey
from lib.groupClass import Group
from blueprints.dialog import dialog
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.secret_key= os.getenv('SECRET_KEY')
# print("Secret Key Loaded:", app.secret_key)  # Debugging line to confirm secret key is loaded
app.register_blueprint(auth)
app.register_blueprint(dialog)

@app.route("/")
def home():
    return "Welcome to Zyneriq! Please visit /dashboard to access your dashboard."

@app.route("/apikey")
def apikey():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    api_keys = APIKey.get_api_key_info()
    groups = Group.get_groups()
    
    return render_template("apikey.html",session=session,api_keys=api_keys,groups=groups)

@app.route("/dashboard")
def dashboard(): 
    
    if not session.get('authenticated'):
        print(session)  # Debugging line to check session contents
        return redirect(url_for('login'))
    else:
        return render_template("dashboard.html",session=session,username=session.get('username'))   

@app.route("/apikey/row") 
def apikey_row():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    api_key_hash = request.args.get('hash')
    if not api_key_hash:
        return {'error': 'API key hash is required'}, 400  
    api_keys_ob = APIKey(api_key_hash)
    if api_keys_ob.collection._data is None:
        return {'error': 'API key not found'}, 404
    print(api_keys_ob.collection._data)  # Debugging line to check API key data
    groups = Group.get_groups()
    return render_template("apikey/api-table.html", api_key=api_keys_ob.collection._data, groups=groups)
@app.route("/profile")
def profile():
    return render_template("profile.html")  

@app.route("/billing")
def billing():
    return render_template("billing.html")  
@app.route("/login")
def login():
    return render_template("login.html")    
@app.route("/signup")
def signup():
    return render_template("signup.html")
if __name__ == "__main__":
    app.run(debug=True)