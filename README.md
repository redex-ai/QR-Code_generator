# QR code generator using Python

This script sets up a Django web server to collect input URLs from a webpage and generate QR codes.

### Prerequisites

- Python 3
- Django
- qrcode

### Libraries Used

- [Django](https://www.djangoproject.com/)
- [qrcode](https://github.com/lincolnloop/python-qrcode)

### To install required external modules

Run the following command to install the required modules:

```shell
pip install django qrcode
```

### How to run the script

1. Clone the repository
2. Navigate to the project directory
3. Run the following command to start the Django server:

```shell
python manage.py runserver
```

4. Open your web browser and go to `http://localhost:8000`
5. Enter the desired URL and click on the 'Generate QR Code' button
6. The QR code will be displayed on the webpage

### Screenshot showing the sample use of the script

![Sample QR Code](output.png)

## Author

[Vikrant](https://github.com/vikrant-v28)
