import qrcode

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    input_URL = request.form['url']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color='red', back_color='white')
    img.save('url_qrcode.png')

    return qr.data_list


if __name__ == '__main__':
    app.run(debug=True)
