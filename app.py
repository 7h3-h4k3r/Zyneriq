from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Zyneriq! Please visit /dashboard to access your dashboard."

@app.route("/apikey")
def apikey():
    return render_template("apikey.html")

@app.route("/dashboard")
def dashboard():    
    return render_template("dashboard.html")    
@app.route("/profile")
def profile():
    return render_template("profile.html")  

@app.route("/billing")
def billing():
    return render_template("billing.html")  
@app.route("/login")
def login():
    return render_template("iot-auth-v2.html", otop=False)    
@app.route("/signin")
def signin():
    return render_template("signin.html", otop=True)
if __name__ == "__main__":
    app.run(debug=True)