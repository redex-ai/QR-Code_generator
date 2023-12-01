import qrcode
import os
import sys

# Get URL from the first command line argument or environment variable
input_URL = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('QR_URL', 'https://www.example.com/')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

# convert into image
img = qr.make_image(fill_color='black', back_color='white')
img.save('url_qrcode.png')

print(f'QR code generated for: {input_URL}')
