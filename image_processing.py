from PIL import Image
from PIL.ExifTags import GPSTAGS
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

def get_exif_data(image_file):
    """ Get EXIF data from image file if available, as well as dimensions """

    img = Image.open(image_file)
    [img_width, img_height] = img.size

    exif_data = img._getexif()

    exposure_calc = exif_data and round(1/exif_data.get(EXIF_DATA_CODES['ExposureTime']))
    location_data = exif_data and exif_data.get(EXIF_DATA_CODES['GPSInfo'])

    gps_coords = (to_dec_deg(location_data[2]),to_dec_deg(location_data[4]))

    image_data_from_file = {
        'width_px': img_width,
        'height_px': img_height,
        'device_manufacturer': exif_data and exif_data.get(EXIF_DATA_CODES['Make']),
        'device_model': exif_data and exif_data.get(EXIF_DATA_CODES['Model']),
        'focal_length': exif_data and exif_data.get(EXIF_DATA_CODES['FocalLength']),
        'f_stop': exif_data and exif_data.get(EXIF_DATA_CODES['ApertureValue']),
        'exposure': exposure_calc,
        'location':gps_coords,
        'taken_at': exif_data and exif_data.get(EXIF_DATA_CODES['DateTime'])
    }


    return image_data_from_file



    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    gps_info = {}
    for key in exif_table['GPSInfo'].keys():
        decode = GPSTAGS.get(key,key)
        gps_info[decode] = exif_table['GPSInfo'][key]
    return gps_info