from flask import Flask, render_template, request, redirect, url_for
import qrcode
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            img = qrcode.make(url)
            img_bytes = io.BytesIO()
            img.save(img_bytes)
            img_bytes.seek(0)
            return redirect(url_for('qr_code'))
    return render_template('home.html')

@app.route('/qr_code')
def qr_code():
    # Assuming 'img_bytes' is passed to the template for display
    return render_template('qr_code.html', image=img_bytes)

if __name__ == '__main__':
    app.run(debug=True)
