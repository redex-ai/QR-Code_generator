FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir qrcode

# Run qr_code_script.py when the container launches
CMD ["python", "./qr_code_script.py"]
