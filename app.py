from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig


app = Flask(__name__)


db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    _id = db.Column("id",db.Integer, primary_key = True)
    username = db.Column("username",db.String(80), unique = True)
    password = db.Column("password",db.String(120))

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
@app.route("/")
def login():
    return render_template("index.html", info = "")
    #login page starts when browser launched

@app.route("/form_login",methods=['POST','GET'])
def log():
    #when login button clicked
    user = request.form['username']
    password = request.form['password']
    db_user = User.query.filter_by(username=user).first()
    #takes information from text boxes
    if db_user:
        if db_user.password == password:
            return render_template("home.html", name = user)
    return render_template("index.html",info='Invalid User or Password')

@app.route("/form_signUp",methods = ["POST","GET"])
def load_signup():
    #if signup button clicked
    return render_template("signUp.html") #go to signup page

@app.route("/form_signUpNow",methods=["POST","GET"])
def sign_up_now():
    #if signupnow button clicked
    user = request.form["new_username"]
    password = request.form["new_password"]
    #get information from textboxes
    dbUser = User.query.filter_by(username=user).first()
    if user == "":
        #check if entered username
        return render_template("signUp.html",info = "Enter Username and Password")
    if dbUser:
        return render_template("signUp.html", info = "this User already exists")
    else:
        if password == "":
            return render_template("signUp.html",info = "Enter Password")
        new_user = User(user,password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("index.html",info = "You have been saved as a user, Please log in")

@app.route("/form_back",methods=["POST","GET"])
def back():
    #if back button picked
    return login() #return to login page




if __name__ == "__main__":
    app.run()