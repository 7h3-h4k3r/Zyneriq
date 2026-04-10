from flask import Flask, render_template ,session, redirect, url_for
from blueprints.authentication import auth 
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
        return redirect(url_for('login'),session=session)
    return render_template("apikey.html")

@app.route("/dashboard")
def dashboard(): 
    
    if not session.get('authenticated'):
        print(session)  # Debugging line to check session contents
        return redirect(url_for('login'))
    else:
        return render_template("dashboard.html",session=session,username=session.get('username'))    
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