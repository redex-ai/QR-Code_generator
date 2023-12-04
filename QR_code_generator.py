import qrcode
import logging

# Configure basic logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Enter url of any website here.
input_URL = "https://www.google.com/"

try:
    logging.debug('Starting QR code generation.')

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
    logging.error(f'An error occurred during QR code generation: {e}')

print(qr.data_list)
