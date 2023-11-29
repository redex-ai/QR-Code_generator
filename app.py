from flask import Flask, render_template, request
import os
import qrcode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the URL from the form
        url = request.form.get('url')

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Save the QR code image to a file
        img.save('static/qr_code.png')

        # Display the QR code image
        return render_template('qr_code.html', qr_code='static/qr_code.png')

    # Show the URL input form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)