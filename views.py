from django.http import JsonResponse
import qrcode
from io import BytesIO
from base64 import b64encode


def generate_qr_code(request):
    # Get the URL from the request
    url = request.GET.get('url', '')

    # Generate QR code
    if url:
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

        response_data = {
            'qr_code': image_base64
        }
        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'No URL provided'}, status=400)
