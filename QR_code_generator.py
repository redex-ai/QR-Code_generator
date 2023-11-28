import qrcode

from django.http import HttpResponse
from django.shortcuts import render


def generate_qr_code(request):
    if request.method == 'POST':
        input_URL = request.POST.get('url')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )

        qr.add_data(input_URL)
        qr.make(fit=True)

        # convert into image
        img = qr.make_image(fill_color='red', back_color='white')
        img.save('url_qrcode.png')

        return HttpResponse('QR code generated successfully!')

    return render(request, 'generate_qr_code.html')
