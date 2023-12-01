# QR code generator using Python
This script takes a link of any URL and generates a `QR code` corresponding to it. Now with added logging functionality to track the process.

### Prerequisites
`Python 3`

### Library Used
* [qrcode](https://github.com/lincolnloop/python-qrcode)

### To install required external modules
Run `pip install qrcode`

### How to run the script
- Provide your desired URL in the script
- Execute `python3 QR_code_generator.py`

### Logging
The script logs its progress in `qr_generation.log` file. It includes information about the start of the process, the input URL, any errors encountered, and the successful saving of the QR code image. The log file rotates after reaching a size of 5KB and keeps a backup count of 2.

To change the log level, modify the `level` parameter in the `basicConfig` method within the script.

### Screenshot showing the sample use of the script
<p align="center">
  <a href="output 1.png"><img src="https://user-images.githubusercontent.com/85709371/151921721-132e76c1-1604-49ad-9234-1ef3cc9ac45b.png" alt="url_qrcode"></a>
</p>

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
