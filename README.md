# QR code generator using Python
This script takes one or more links of URLs and generates separate `QR codes` corresponding to each URL.

### Prerequisites

- `Python 3`

### Library Used

- [qrcode](https://github.com/lincolnloop/python-qrcode)

### To install required external modules

Run `pip install qrcode`

### How to run the script

- Provide one or more URLs as command line arguments or in a file.
  - Command line syntax: `python3 QR_code_generator.py url1 url2 url3 ...`
  - File format: Each URL should be on a separate line.

- The script will generate a separate QR code image for each URL.
- The generated QR code images will be named using the following convention:
  - For URL `https://www.example.com`, the image will be named `url_qrcode_1.png`
  - For URL `https://www.google.com`, the image will be named `url_qrcode_2.png`
  - And so on...

### Screenshot showing the sample use of the script

<p align="center">
  <a href="output 1.png"><img src="https://user-images.githubusercontent.com/85709371/151921721-132e76c1-1604-49ad-9234-1ef3cc9ac45b.png" alt="url_qrcode"></a>
</p>

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)