""" models for pixly """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """ connects this database to the provided flask app"""
    app.app_context().push()
    db.app = app
    db.init_app(app)

class Image(db.Model):
    """ model for Images table"""

    __tablename__ = "images"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement=True)
    upload_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now())
    times_viewed = db.Column(
        db.Integer,
        default = 0,
        nullable=False)
    file_name = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )
    caption = db.Column(
        db.String(100),
        nullable= True,
    )
    photographer = db.Column(
        db.String(50),
        nullable=True
    )
    title = db.Column(
        db.String(50),
        nullable=False
    )









