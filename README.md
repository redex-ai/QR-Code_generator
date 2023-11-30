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
- Execute `python3 QR_code_generator.py`

### Command Line Syntax

```
python3 QR_code_generator.py url1 url2 url3
```

### File Format

Create a file `urls.txt` and add one URL per line:

```
https://www.google.com/
https://www.github.com/
https://www.linkedin.com/
```

### Naming Convention for Generated QR Code Images

The generated QR code images will be named using a combination of the URL and an index. For example, if the URL is `https://www.google.com/` and the index is 1, the image will be named `google_1_qrcode.png`.

### Screenshot showing the sample use of the script

<p align="center">
  <a href="output 1.png"><img src="https://user-images.githubusercontent.com/85709371/151921721-132e76c1-1604-49ad-9234-1ef3cc9ac45b.png" alt="url_qrcode"></a>
</p>

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)