from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO


def qr_code_view(request):
    if request.method == 'GET':
        # Render the form template
        return render(request, 'qr_form.html')
    elif request.method == 'POST':
        # Process the form data
        data = request.POST.get('data')
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
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        # Send the QR code image back to the template
        image = buffer.getvalue()
        buffer.close()
        response = HttpResponse(image, content_type='image/png')
        return response

# You may need to add additional imports or modify the code depending on your specific Django setup and requirements.
