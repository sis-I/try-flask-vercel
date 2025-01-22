from flask import Flask
from flask_cors import CORS
from flask_session import Session


app = Flask(__name__)

@app.route("/")
def index():
  return "Index Page"

if __name__ == '__main__':
  app.run(debug=True)