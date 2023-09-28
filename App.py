from flask import render_template,flash,Flask,request,redirect,session
#from Functions.functions import ValidateUser
from flask_session import Session

app = Flask(__name__,static_folder='static', template_folder="templates")
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/")
def Index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)