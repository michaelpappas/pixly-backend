import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, connect_db, Image, EXIFData, Tag, ImageTag
from pixly_aws import upload_image_to_aws
from shortuuid import uuid
from image_processing import get_exif_data, make_thumbnail, convert_to_grayscale, resize_image

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

    search_term  = request.args.get("searchTerm") # search term or None

    is_filtering_width = request.args.get('isFilteringWidth') == 'true'
    is_filtering_height = request.args.get('isFilteringHeight') == 'true'

    min_width = request.args.get('minWidth') # '' or an integer string e.g. '10'
    min_width = int(min_width) if is_filtering_width and min_width.isnumeric() else 0

    max_width = request.args.get('maxWidth') # '' or an integer string e.g. '10'
    max_width = int(max_width) if is_filtering_width and max_width.isnumeric() else float('inf')

    min_height = request.args.get('minHeight') # '' or an integer string e.g. '10'
    min_height = int(min_height) if is_filtering_height and min_height.isnumeric() else 0

    max_height = request.args.get('maxHeight') # '' or an integer string e.g. '10'
    max_height = int(max_height) if is_filtering_height and max_height.isnumeric() else float('inf')

    # Filter by EXIF data
    images = db.session.query(Image).join(EXIFData)

    images = images.filter(EXIFData.width_px >= min_width)
    images = images.filter(EXIFData.width_px <= max_width)

    images = images.filter(EXIFData.height_px >= min_height)
    images = images.filter(EXIFData.height_px <= max_height)

    if search_term:
        images = images.filter(Image.title.ilike(f"%{search_term}%"))

    images = images.order_by(Image.id).all()

    serialized = [image.serialize() for image in images]

    return jsonify(images=serialized)


@app.route("/api/images/<int:id>")
def get_image(id):
    """ grabs an image from the database and returns as json """

    image = Image.query.get_or_404(id)

    image_exif_data = image.exif_data[0]
    serialized_image = image.serialize()
    serialized_exif_data = image_exif_data.serialize()
    serialized_exif_data.pop("image_id")
    serialized_image['exif_data'] = serialized_exif_data

    return jsonify(image=serialized_image)


@app.post("/api/images")
def upload_image():
    """ post route for uploading image from front end """

    image_file = request.files.get('imgFile')
    file_extension = image_file.filename.split('.')[-1]
    file_name = f'img_{uuid()}.{file_extension}'

    form_data = request.form

    filter = form_data['filter'] # '', 'bw'
    resize_percentage = int(form_data['resize']) # 100, 75, 50, 25

    if filter == 'bw':
        image_file = convert_to_grayscale(image_file)

    if resize_percentage != 100:
        image_file = resize_image(image_file, resize_percentage)

    upload_image_status = upload_image_to_aws(
        image_file,
        BUCKET_ORIGINALS_FOLDER,
        file_name
    )

    thumbnail_file = make_thumbnail(image_file)

    upload_thumbnail_status = upload_image_to_aws(
        thumbnail_file,
        BUCKET_THUMBNAILS_FOLDER,
        file_name
    )
    if not upload_image_status or not upload_thumbnail_status:
        return (jsonify(error="File failed to upload."), 500)

    image = Image(
        file_name=file_name,
        title=form_data["title"],
        caption=form_data["caption"],
        photographer=form_data["photographer"])

    db.session.add(image)
    db.session.commit()

    image_id = image.id
    image_data = get_exif_data(image_file)


    image_exif_data = EXIFData(
        image_id = image_id,
        height_px = image_data['height_px'],
        width_px = image_data['width_px'],
        device_manufacturer = image_data['device_manufacturer'],
        device_model = image_data['device_model'],
        focal_length = image_data['focal_length'],
        f_stop = image_data['f_stop'],
        exposure = image_data['exposure'],
        location = image_data['location'],
        taken_at = image_data['taken_at'],
    )

    db.session.add(image_exif_data)
    db.session.commit()

    serialized = image.serialize()

    return (jsonify(image = serialized),201)