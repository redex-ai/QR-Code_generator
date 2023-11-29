import qrcode
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def generate_qr_code(url, fill_color='black', back_color='white'):
    logging.info('Generating QR code for URL: %s', url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image with a unique filename or return the image object
    img.save('generated_qr.png')
    logging.info('QR code generated and saved as generated_qr.png')
    return img

# Example usage
# generate_qr_code('https://www.example.com/')
