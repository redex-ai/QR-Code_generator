from django import forms


class URLInputForm(forms.Form):
    url = forms.URLField(label='Enter URL', required=True, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))
