from flask import Flask, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the QR Code Generator!'

@app.route('/generate-qr')
def generate_qr():
    # Data to be encoded
    data = 'https://www.example.com'
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route('/qr-code')
def serve_qr_code():
    # This should be the path to the saved QR code image
    path_to_qr_code_image = 'path/to/qr_code.png'
    return send_file(path_to_qr_code_image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)