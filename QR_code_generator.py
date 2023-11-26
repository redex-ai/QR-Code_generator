import qrcode
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)


def generate_qr_code(url):
    logging.info('Generating QR code for URL: %s', url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color='red', back_color='white')
    logging.info('QR code generation successful')
    return img


# Example usage:
if __name__ == '__main__':
    # Enter url of any website here.
    input_URL = 'https://www.google.com/'
    logging.info('Application started')
    img = generate_qr_code(input_URL)
    img.save('url_qrcode.png')
    logging.info('QR code saved as url_qrcode.png')
