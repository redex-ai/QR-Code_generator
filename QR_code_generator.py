import qrcode
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Enter URL of any website here.
input_URL = "https://www.google.com/"

# Log start of QR code generation process
logging.info("Starting QR code generation process")

try:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    # Convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")

    # Log end of QR code generation process
    logging.info("QR code generation process completed successfully")

    print(qr.data_list)

except Exception as e:
    # Log any potential errors
    logging.error(f"An error occurred during QR code generation: {str(e)}")
