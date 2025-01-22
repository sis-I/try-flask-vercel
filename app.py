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


app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

@app.route("/")
def index():
  print(session.get("name"))
  return render_template("index.html", name=session.get("name"))


@app.route("/login", methods=["GET", "POST"])
def login():

  if request.method == "POST":
    session["name"] = request.form.get("name")
    print(request.form.get("name"))
    return redirect("/")
  
  return render_template("login.html")

@app.route("/logout")
def logout():

  session.clear()
  return redirect("/")


if __name__ == '__main__':

  app.run(debug=True)