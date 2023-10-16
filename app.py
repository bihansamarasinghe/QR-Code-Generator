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
