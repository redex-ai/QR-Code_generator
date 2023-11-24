from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import qrcode
from io import BytesIO

@require_http_methods(['GET', 'POST'])
def qr_code_generator(request):
    if request.method == 'GET':
        # Render the form for user input
        return render(request, 'qr_form.html')
    elif request.method == 'POST':
        # Generate QR code
        url = request.POST.get('url', '')
        if not url:
            return JsonResponse({'error': 'No URL provided'}, status=400)

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

        response = HttpResponse(buffer, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=qr.png'
        return response

# You can add other views here as needed.
