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

if __name__ == "__main__":
    app.run(host="127.0.0.1" ,port=8000 ,debug=True)  # 启动这个应用