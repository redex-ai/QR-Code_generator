import qrcode
from io import BytesIO


def generate_qr_code(input_url):
    # Initialize QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    # Add data to the QR Code
    qr.add_data(input_url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save it to a BytesIO object to avoid writing to disk
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)

    return img_bytes
