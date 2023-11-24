import qrcode
from io import BytesIO


def generate_qr_code(url):
    # Initialize the QRCode object.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    # Add the URL data to the QRCode object.
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance.
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the image to a BytesIO object to return as data.
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)

    return img_bytes

# Example usage:
# with open('url_qrcode.png', 'wb') as f:
#     img_data = generate_qr_code('https://www.example.com')
#     f.write(img_data.read())
