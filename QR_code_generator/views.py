from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def generate_qr(request):
    if request.method == 'GET':
        # Display the form for QR code generation
        logger.info('Displaying QR code generation form')
        return render(request, 'qr_form.html')
    elif request.method == 'POST':
        # Generate the QR code
        data = request.POST.get('data', '')
        logger.info('Received data to generate QR code: %s', data)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        logger.info('QR code generated successfully')
        return response
    else:
        logger.error('Invalid request method: %s', request.method)
        return HttpResponse(status=405)