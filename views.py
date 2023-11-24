from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO
from base64 import b64encode


def input_url_form(request):
    if request.method == 'GET':
        # Render the form for input URL
        return render(request, 'input_form.html')
    elif request.method == 'POST':
        # Generate QR code
        url = request.POST.get('url', '')
        if not url:
            return HttpResponse('No URL provided', status=400)

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
        img_str = b64encode(buffer.getvalue()).decode('utf-8')

        # Return QR code image as a data URL
        return HttpResponse(f'<img src="data:image/png;base64,{img_str}" alt="QR Code" />')
    else:
        return HttpResponse('Invalid HTTP method', status=405)
