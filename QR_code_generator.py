import qrcode
from io import BytesIO


def generate_qr_code(input_URL):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color='red', back_color='white')

    # Save the image to a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)

    return img_bytes
