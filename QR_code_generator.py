import qrcode
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def generate_qr_code(input_URL):
    logging.info('Starting QR code generation.')
    logging.debug('URL provided: %s', input_URL)
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

    # Save the QR code image to a file or do something else with the image object
    # img.save("url_qrcode.png")
    logging.info('QR code generation completed successfully.')

    return img
