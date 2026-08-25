from flask import Flask

app=Flask(__name__)


@app.route("/")
def welcome():
    return "welcomee hereee you know "

@app.route("/index")
def index():
    return "welcomee hereee  to indexx you know "

if __name__=="__main__":
    app.run(debug=True)