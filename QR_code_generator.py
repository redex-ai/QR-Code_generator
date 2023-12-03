import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler('qr_code_generator.log', maxBytes=5000, backupCount=2),
                              logging.StreamHandler()])

# Enter url of any website here.
input_URL = "https://www.google.com/"

try:
    logging.debug('Initializing QR code generation.')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    logging.debug('Adding data to QR code.')
    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    logging.debug('Converting QR code data to an image.')
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")
    logging.info('QR code image saved successfully.')

except Exception as e:
    logging.exception('An error occurred while generating the QR code: %s', e)

logging.debug('QR code data list: %s', qr.data_list)
print(qr.data_list)
