import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logging.basicConfig(handlers=[RotatingFileHandler('qr_generation.log', maxBytes=10000, backupCount=3)],
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Enter url of any website here.
input_URL = "https://www.google.com/"

logging.info('Starting QR code generation process.')
logging.debug(f'Input URL: {input_URL}')

try:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    logging.debug('QR code instance created.')

    qr.add_data(input_URL)
    logging.debug('Data added to QR code.')

    qr.make(fit=True)
    logging.debug('QR code fitting is done.')

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")
    logging.info('QR code image saved successfully.')
except Exception as e:
    logging.error(f'Error during QR code generation: {e}')

logging.debug(f'QR code data list: {qr.data_list}')
print(qr.data_list)
