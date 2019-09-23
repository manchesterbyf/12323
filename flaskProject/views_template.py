from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "laobian"
    return render_template("index.html",**locals())

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/base/")
def base():
    return render_template("base.html")

@app.route("/index/")
def exindex():
    return render_template("ex_index.html")
import time
@app.route("/userinfo/")
def userinfo():

    return render_template("userinfo.html")



if __name__ == "__main__":
    app.run(host="127.0.0.1" ,port=8000 ,debug=True)  # 启动这个应用