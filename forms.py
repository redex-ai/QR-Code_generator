from django import forms


class URLInputForm(forms.Form):
    url = forms.URLField(label='Enter URL to generate QR code', required=True)
