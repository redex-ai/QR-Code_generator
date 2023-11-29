from django.test import TestCase, Client
from django.urls import reverse
import io
from PIL import Image


class QRCodeGeneratorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.generate_url = reverse('generate_qr')

    def test_get_generate_qr_page(self):
        response = self.client.get(self.generate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qr_code_form.html')

    def test_post_generate_qr_valid_url(self):
        valid_url = 'https://www.example.com'
        response = self.client.post(self.generate_url, {'url': valid_url})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/png')
        image_stream = io.BytesIO(response.content)
        image = Image.open(image_stream)
        self.assertEqual(image.format, 'PNG')

    def test_post_generate_qr_invalid_url(self):
        invalid_url = 'not-a-valid-url'
        response = self.client.post(self.generate_url, {'url': invalid_url})
        self.assertEqual(response.status_code, 400)
        self.assertFormError(response, 'form', 'url', 'Enter a valid URL.')
