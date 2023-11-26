from django.http import HttpResponse
import qrcode
from io import BytesIO


def generate_qr(request, data):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save it to a stream
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # Send the response with the image
    return HttpResponse(buffer, content_type='image/png')

# Example usage: the 'data' parameter will come from the URL
# def my_view(request):
#     data = request.GET.get('data', 'No data')
#     return generate_qr(request, data)
