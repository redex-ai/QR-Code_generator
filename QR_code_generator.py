import qrcode
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def generate_qr_code(url):
    logging.info(f'Generating QR code for URL: {url}')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    logging.info('QR code generation successful')
    return img

# Example usage:
# img = generate_qr_code("https://www.google.com/")
# img.save("url_qrcode.png")
# logging.info("QR code generated and saved as 'url_qrcode.png'")
