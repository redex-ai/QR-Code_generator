import qrcode


def generate_qr_code(url, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save('static/url_qrcode.png')

    return 'static/url_qrcode.png'


if __name__ == '__main__':
    # Example usage: Generate a QR code for a given URL
    import sys
    if len(sys.argv) > 1:
        input_url = sys.argv[1]
        generate_qr_code(input_url)
        print(f'QR code generated for {input_url} and saved as static/url_qrcode.png')
    else:
        print('Usage: python QR_code_generator.py <url>')
