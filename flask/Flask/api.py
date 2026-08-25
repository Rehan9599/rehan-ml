from flask import Flask,render_template,request,redirect,url_for


app=Flask(__name__)

msgs=[]

@app.route("/")
def welcome():
    return "<html> <H1> heyyy welcome to my to-do list app</H1> </html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        message=request.form['message']
        id=request.form['id']
        msgs.append({name:message})
    return render_template('form.html')


@app.route('/show/<int:msgid>', methods=['GET'])
def show(msgid):
    msg=msgs[msgid]
    return render_template('msgs.html',msg=msg)



if __name__=="__main__":
    app.run(debug=True)