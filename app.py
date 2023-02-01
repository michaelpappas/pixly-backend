import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, connect_db, Image, EXIFData, Tag, ImageTag

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = (
  os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
toolbar = DebugToolbarExtension(app)

# debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/api/images")
def helloWorld():
  """ grabs all images from the database and returns as json """

  images = [{"image": "image.jpeg", "image_data": "text", "url": "aws/s3/teamwork.jpeg"}]
  return jsonify(images = images)