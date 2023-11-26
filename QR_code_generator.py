import qrcode


def generate_qr_code(url):
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
    return img


# Example usage:
if __name__ == '__main__':
    # Enter url of any website here.
    input_URL = 'https://www.google.com/'
    img = generate_qr_code(input_URL)
    img.save('url_qrcode.png')
    print('QR code generated and saved as url_qrcode.png')
