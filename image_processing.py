from PIL import Image

EXIF_DATA_CODES = {
    'Make': 271,
    'Model': 272,
    'FocalLength': 37386,
    'ApertureValue': 37378,
    'ExposureTime': 33434,
    'GPSInfo': 34853,
    'DateTime': 306
}

def get_exif_data(image_file):
    """ Get EXIF data from image file if available, as well as dimensions """

    img = Image.open(image_file)
    [img_width, img_height] = img.size

    exif_data = img._getexif()

    image_data_from_file = {
        'width_px': img_width,
        'height_px': img_height,
        'device_manufacturer': exif_data and exif_data.get(EXIF_DATA_CODES['Make']),
        'device_model': exif_data and exif_data.get(EXIF_DATA_CODES['Model']),
        'focal_length': exif_data and exif_data.get(EXIF_DATA_CODES['FocalLength']),
        'f_stop': exif_data and exif_data.get(EXIF_DATA_CODES['ApertureValue']),
        'exposure': exif_data and exif_data.get(EXIF_DATA_CODES['ExposureTime']),
        'location': exif_data and exif_data.get(EXIF_DATA_CODES['GPSInfo']),
        'taken_at': exif_data and exif_data.get(EXIF_DATA_CODES['DateTime'])
    }

    return image_data_from_file