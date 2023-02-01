import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, connect_db, Image, EXIFData, Tag, ImageTag
from pixly_aws import upload_image_to_aws
from shortuuid import uuid

BUCKET_THUMBNAILS_FOLDER = 'pixly/images/thumbnails/'
BUCKET_ORIGINALS_FOLDER = 'pixly/images/originals/'

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
def get_images():
    """ grabs all images from the database and returns as json """

    images = Image.query.order_by(Image.id).all()

    serialized = [image.serialize() for image in images]

    return jsonify(images=serialized)


@app.route("/api/images/<int:id>")
def get_image(id):
    """ grabs an image from the database and returns as json """

    image = Image.query.get_or_404(id)

    return jsonify(image=image.serialized())

@app.post("/api/images")
def upload_image():
    """ post route for uploading image from front end """

    image = request.files.get('File')
    file_extension = image.filename.split('.')[-1]
    file_name = f'img_{uuid()}.{file_extension}'

    upload_image_to_aws(image, BUCKET_ORIGINALS_FOLDER, file_name)

    # Test if uploads worked and then add to database

    return "image"