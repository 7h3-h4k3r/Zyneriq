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
    return render_template("login.html", otop=False)    
@app.route("/signup")
def signup():
    return render_template("signup.html", otop=True)
if __name__ == "__main__":
    app.run(debug=True)