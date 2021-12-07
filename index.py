from flask import Flask,render_template,jsonify,request,flash
from flask.templating import render_template_string
from db import Database

app = Flask(__name__)
logindb=Database.Database()
app.config["SECRET_KEY"] = "ABCD"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/1")
def dong():
    return render_template("index.html")

@app.route("/post", methods= ['POST'])
def post():
    userID = request.form['inputID']
    userPW = request.form['inputPW']
    msg = logindb.selectAllJson()

    for i in msg:
        if i[1] == userID and i[2] == userPW:
            return render_template('index.html')

    flash('다시 시도해 주세요')
    return render_template('login.html') 



if __name__ == "__main__":
    app.run(host = "0.0.0.0")

