import os

from flask import (Flask, 
                   render_template, 
                   redirect,
                   request, 
                   session,
                   jsonify,
                   send_from_directory
                  )
from flask_cors import CORS
from flask_session import Session
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = os.getenv("SECRET_KEY") or 'dksdjf)9dewjj*edf'

app.config['SESSION_TYPE'] =  'filesystem'
app.congig['SESSION_FILE_DIR'] = '/flask_session'
app.config['SESSION_PERMANENT'] = False
Session(app)

@app.route("/", methods=["GET",])
def index():
  print(session.get("name"))
  return render_template("index.html", name=session.get("name"))


@app.route("/login", methods=["GET", "POST"])
def login():

  if request.method == "POST":
    session["name"] = request.form.get("name")
    print(request.form.get("name"))
    res  = redirect("/")
    
    print(res.status_code)
    return redirect("/")
  
  return render_template("login.html")

@app.route("/logout")
def logout():

  session.clear()
  return redirect("/")


if __name__ == '__main__':

  app.run(debug=True)