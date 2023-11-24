from django.http import JsonResponse
from django.shortcuts import render
import qrcode
from io import BytesIO
from base64 import b64encode


def handle_qr_request(request):
    if request.method == 'GET':
        # Render the form for user input
        return render(request, 'qr_form.html')
    elif request.method == 'POST':
        # Generate QR code
        data = request.POST.get('data')
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = b64encode(buffered.getvalue()).decode('utf-8')

            return JsonResponse({'qr_code': img_str})
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
