import qrcode


def generate_qr_code(input_URL, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    return img

# Example usage:
# img = generate_qr_code('https://www.example.com/')
# img.save('url_qrcode.png')
