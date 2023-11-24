from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO
from base64 import b64encode


def qr_code_generator(request):
    if request.method == 'POST':
        # Get the URL from the POST request
        url = request.POST.get('url', '')

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
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        image_base64 = b64encode(image_png)
        image_base64 = image_base64.decode('utf-8')
        context = {'qr_code': image_base64}

        return render(request, 'qr_code_page.html', context)

    return render(request, 'qr_code_page.html')
