from django.shortcuts import render
from django.http import HttpResponse
import io
from .QR_code_generator import generate_qr_code
from django import forms


class URLInputForm(forms.Form):
    url = forms.URLField(label='Enter URL')


def qr_code_view(request):
    if request.method == 'POST':
        form = URLInputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            qr_image = generate_qr_code(url)
            response = HttpResponse(content_type='image/png')
            qr_image.save(response, 'PNG')
            return response
    else:
        form = URLInputForm()

    return render(request, 'qr_code_form.html', {'form': form})
