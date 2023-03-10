import io
from PIL import Image
from lat_lon_parser import to_dec_deg

EXIF_DATA_CODES = {
    'Make': 271,
    'Model': 272,
    'FocalLength': 37386,
    'ApertureValue': 37378,
    'ExposureTime': 33434,
    'GPSInfo': 34853,
    'DateTime': 306
}

GPS_TAG_CODES = {
    'GPSLatitudeRef': 1,
    'GPSLatitude': 2,
    'GPSLongitudeRef': 3,
    'GPSLongitude': 4
}

THUMBNAIL_MAX_SIZE = (200, 200)

def get_exif_data(image_file):
    """ Get EXIF data from image file if available, as well as dimensions """
    img = Image.open(image_file)
    (img_width, img_height) = img.size

    exif_data = img._getexif()
    exposure_calc = (
        exif_data and
        exif_data.get(EXIF_DATA_CODES['ExposureTime']) and
        round(1/exif_data.get(EXIF_DATA_CODES['ExposureTime']))
    )

    location_data = exif_data and exif_data.get(EXIF_DATA_CODES['GPSInfo'])

    is_valid_location_data = bool(
        location_data and
        GPS_TAG_CODES['GPSLatitudeRef'] in location_data and
        GPS_TAG_CODES['GPSLatitude'] in location_data and
        GPS_TAG_CODES['GPSLongitudeRef'] in location_data and
        GPS_TAG_CODES['GPSLongitude'] in location_data
    )

    gps_coords = None

    if is_valid_location_data:
        lat_ref = location_data[GPS_TAG_CODES['GPSLatitudeRef']] # N or S
        (lat_d, lat_m, lat_s) = location_data[GPS_TAG_CODES['GPSLatitude']]

        lon_ref = location_data[GPS_TAG_CODES['GPSLongitudeRef']] # E or W
        (lon_d, lon_m, lon_s) = location_data[GPS_TAG_CODES['GPSLongitude']]

        lat_dec_deg = to_dec_deg(lat_d, lat_m, lat_s) * (-1 if lat_ref == 'S' else 1)
        lon_dec_deg = to_dec_deg(lon_d, lon_m, lon_s) * (-1 if lon_ref == 'W' else 1)

        gps_coords = f'{lat_dec_deg},{lon_dec_deg}'

    image_data_from_file = {
        'width_px': img_width,
        'height_px': img_height,
        'device_manufacturer': exif_data and exif_data.get(EXIF_DATA_CODES['Make']),
        'device_model': exif_data and exif_data.get(EXIF_DATA_CODES['Model']),
        'focal_length': (
            exif_data and
            exif_data.get(EXIF_DATA_CODES['FocalLength']) and
            int(exif_data.get(EXIF_DATA_CODES['FocalLength']))
        ),
        'f_stop': (
            exif_data and
            exif_data.get(EXIF_DATA_CODES['ApertureValue']) and
            float(exif_data.get(EXIF_DATA_CODES['ApertureValue']))
        ),
        'exposure': exposure_calc,
        'location': gps_coords,
        'taken_at': exif_data and exif_data.get(EXIF_DATA_CODES['DateTime'])
    }

    return image_data_from_file

def make_thumbnail(file):
    """ Given an image file, create a thumbnail for it and return as an
    in-memory file """
    img = Image.open(file)
    img.thumbnail(THUMBNAIL_MAX_SIZE)

    in_mem_file = io.BytesIO()
    img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)

    return in_mem_file

def convert_to_grayscale(image_file):
    """ Given an image file, convert it to grayscale """

    img = Image.open(image_file)
    converted_img = img.convert('L')

    in_mem_file = io.BytesIO()
    converted_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)

    return in_mem_file

def resize_image(image_file, percentage):
    """ Given an image file and desired percentage, resize it """

    img = Image.open(image_file)
    (img_width, img_height) = img.size
    new_img_size = (int(img_width * percentage / 100), int(img_height * percentage / 100))
    resized_img = img.resize(new_img_size)

    in_mem_file = io.BytesIO()
    resized_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)

    return in_mem_file