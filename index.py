from flask import Flask,render_template,jsonify,request
from flask.templating import render_template_string
from db import Database

app = Flask(__name__)
logindb=Database.Database()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post", methods= ['POST'])
def post():
    userID = request.form['inputID']
    userPW = request.form['inputPW']
    msg = logindb.insertLogin(userID,userPW)
    return msg

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

