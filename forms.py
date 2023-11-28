from django import forms


class URLInputForm(forms.Form):
    url = forms.CharField(label='Enter URL', max_length=2048)
