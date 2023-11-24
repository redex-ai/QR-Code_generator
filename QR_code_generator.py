import qrcode


def generate_qr_code(input_URL, fill_color='red', back_color='white', file_name='url_qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(file_name)

    return file_name

# Example usage:
# generate_qr_code('https://www.google.com/')
