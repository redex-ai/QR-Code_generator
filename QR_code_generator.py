import qrcode
import sys
import os

# Function to generate QR code
def generate_qr_code(url, index):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the image with a unique name
    filename = f'url_qrcode_{index}.png'
    img.save(filename)
    print(f'QR code generated for: {url} - Saved as: {filename}')

# Main function to process multiple URLs
if __name__ == '__main__':
    # Check if URLs are provided as command-line arguments
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        print('No URLs provided. Please provide URLs as command-line arguments.')
        sys.exit(1)

    # Generate QR code for each URL
    for index, url in enumerate(urls, start=1):
        generate_qr_code(url, index)
