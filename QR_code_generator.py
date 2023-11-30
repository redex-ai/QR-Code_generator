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
# img = generate_qr_code('https://www.example.com/')
# img.save('url_qrcode.png')
