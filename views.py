from django.http import HttpResponse
import qrcode
from io import BytesIO


def generate_qr(request):
    if request.method == 'POST':
        # Extract the URL from the POST request
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

        # Save the generated QR code to a BytesIO object
        response = BytesIO()
        img.save(response)
        response.seek(0)

        # Send the generated QR code back as an image response
        return HttpResponse(response.getvalue(), content_type='image/png')

    else:
        return HttpResponse('Invalid request', status=400)