import qrcode
import sys

# Enter urls of any websites here.
input_URLs = sys.argv[1:]

for i, url in enumerate(input_URLs):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    img.save(f"url_qrcode_{i}.png")

    print(f"QR code generated for URL: {url}")
