import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler('qr_code_generator.log', maxBytes=5*1024*1024, backupCount=3),
                              logging.StreamHandler()])

# Enter url of any website here.
input_URL = "https://www.google.com/"

try:
    logging.info('Starting QR code generation.')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")

    logging.info('QR code generated successfully.')
except Exception as e:
    logging.error('An error occurred while generating the QR code: %s', e)
finally:
    logging.info('QR code generation script has finished execution.')
