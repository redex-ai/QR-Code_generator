from django.http import HttpResponse
import qrcode
from io import BytesIO


def generate_qr(request):
    # Assuming 'data' is the field that contains the string to encode in the QR code
    data = request.GET.get('data', '')

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save the generated QR code in a BytesIO object
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # Send the generated QR code back as an image response
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename=qr.png'
    return response
