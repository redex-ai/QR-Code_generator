from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/qr-form', methods=['GET', 'POST'])
def qr_code_form():
    if request.method == 'POST':
        # Logic for handling QR code generation goes here
        pass
    return render_template('qr_form.html')

if __name__ == '__main__':
    app.run(debug=True)