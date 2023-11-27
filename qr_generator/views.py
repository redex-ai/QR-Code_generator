from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO
from PIL import Image


def generate_qr(request):
    if request.method == 'POST':
        # Extract the URL from the POST request
        input_url = request.POST.get('url', '')

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Save the generated QR code to a BytesIO object
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        # Send the generated QR code back as an image response
        return HttpResponse(buffer, content_type='image/png')

    else:
        # If the request is not POST, display the QR code form
        return render(request, 'qr_form.html')
