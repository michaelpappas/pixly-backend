""" models for pixly """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ connects this database to the provided flask app"""
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Image(db.Model):
    """ model for images table"""

    __tablename__ = "images"

    ###### TABLE COLUMNS ######

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    file_name = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )
    title = db.Column(
        db.String(50),
        nullable=False
    )
    caption = db.Column(
        db.String(100),
        nullable=True,
    )
    upload_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now()
    )
    times_viewed = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )
    photographer = db.Column(
        db.String(50),
        nullable=True
    )

    ###### RELATIONSHIPS ######

    exif_data = db.relationship('EXIFData', backref='image')
    tags = db.relationship('Tag', secondary='images_tags', backref='images')

    ###### INSTANCE METHOD ######

    def __repr__(self):
        return f'<Image {self.id} {self.title} {self.file_name}>'


class EXIFData(db.Model):
    """ Model for exif_data table """

    __tablename__ = 'exif_data'

    ###### TABLE COLUMNS ######

    image_id = db.Column(
        db.Integer,
        db.ForeignKey('images.id', ondelete='CASCADE'),
        primary_key=True
    )
    height_px = db.Column(
        db.Integer,
        nullable=False
    )
    width_px = db.Column(
        db.Integer,
        nullable=False
    )
    device_manufacturer = db.Column(
        db.String(100),
        nullable=True
    )
    device_model = db.Column(
        db.String(100),
        nullable=True
    )
    focal_length = db.Column(
        db.Integer,
        nullable=True
    )
    f_stop = db.Column(
        db.Integer,
        nullable=True
    )
    exposure = db.Column(
        db.Integer,
        nullable=True
    )
    location = db.Column(
        db.String(100),
        nullable=True
    )

    ###### INSTANCE METHODS ######

    def __repr__(self):
        return f'<EXIFData Image {self.image_id}: {self.image.title}>'


class Tag(db.Model):
    """ Model for tags table """

    __tablename__ = 'tags'

    ###### TABLE COLUMNS ######

    name = db.Column(
        db.String(30),
        primary_key = True
    )

    ###### INSTANCE METHODS ######

    def __repr__(self):
        return f'<Tag {self.name}>'


class ImageTag(db.Model):
    """ Model for images - tags association table """

    __tablename__ = 'images_tags'

    ###### TABLE COLUMNS ######

    image_id = db.Column(
        db.Integer,
        db.ForeignKey('images.id', ondelete='CASCADE'),
        primary_key=True
    )
    tag_name = db.Column(
        db.String(30),
        db.ForeignKey('tags.name', ondelete='CASCADE'),
        primary_key=True
    )

    ###### INSTANCE METHODS ######

    def __repr__(self):
        return f'<ImageTag Image {self.image_id}: Tag {self.tag_name}>'
