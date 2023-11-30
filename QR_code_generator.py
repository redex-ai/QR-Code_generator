import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logging.basicConfig(filename='qr_code_generator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Enter url of any website here.
input_URL = "https://www.google.com/"

# Log start of QR code generation
logging.info('Starting QR code generation')

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

# Log successful QR code generation
logging.info('QR code generated successfully')

# Log confirmation of QR code save
logging.info('QR code saved successfully')

# Log end of QR code generation
logging.info('QR code generation completed')

print(qr.data_list)