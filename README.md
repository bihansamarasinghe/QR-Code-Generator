---

# QR Code Generator

This Python script generates a QR code using the `qrcode` library and saves it as an image. The QR code contains a link to your GitHub profile.

## Usage

1. Install the necessary Python libraries:

   ```bash
   pip install qrcode[pil]
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

3. Run the Python script:

   ```bash
   python generate_qrcode.py
   ```

   Replace `"https://github.com/bihansamarasinghe"` with your desired URL.

4. Check the repository for the generated QR code image named `mygithubprofile.png`.

## Code

```python
import qrcode

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=1
)

# Add data to the QR code
data = "https://github.com/bihansamarasinghe"
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("mygithubprofile.png")
```

Replace `"https://github.com/bihansamarasinghe"` with your GitHub profile URL.

---
