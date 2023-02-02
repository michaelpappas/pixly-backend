from PIL import Image


def get_exif_data(image):
    img = Image.open()
    exif_data = img._getexif()

for key, val in exif_data.items():
    if key in ExifTags.TAGS:
        print(f"{ExifTags.TAGS[key]}:{val}")



# GPSInfo:{0: b'\x02\x02\x00\x00', 5: b'\x00', 31: 4.487276765059684}
# ResolutionUnit:2
# ExifOffset:222
# Make:Apple
# Model:iPhone 13 Pro
# Software:15.5
# Orientation:1
# DateTime:2022:08:02 12:56:55
# XResolution:72.0
# YResolution:72.0
# HostComputer:iPhone 13 Pro
# ExifVersion:b'0232'
# ShutterSpeedValue:11.150208855472014
# ApertureValue:2.970853653853539
# DateTimeOriginal:2022:08:02 12:56:55
# DateTimeDigitized:2022:08:02 12:56:55
# BrightnessValue:11.04916051040967
# ExposureBiasValue:0.0
# MeteringMode:5
# ColorSpace:65535
# Flash:16
# FocalLength:9.0
# ExifImageWidth:4032
# ExifImageHeight:3024
# FocalLengthIn35mmFilm:77
# OffsetTime:-07:00
# OffsetTimeOriginal:-07:00
# OffsetTimeDigitized:-07:00
# SubsecTimeOriginal:541
# SubjectLocation:(2013, 1500, 2310, 1327)
# SubsecTimeDigitized:541
# SensingMethod:2
# ExposureTime:0.0004399472063352398
# FNumber:2.8
# SceneType:b'\x01'
# ImageUniqueID:d1a7338a6d6cf00e0000000000000000
# ExposureProgram:2
# ISOSpeedRatings:32
# ExposureMode:0
# WhiteBalance:0
# LensSpecification:(1.5700000524639703, 9.0, 1.5, 2.8)
# LensMake:Apple
# LensModel:iPhone 13 Pro back triple camera 9mm f/2.8
# CompositeImage:2