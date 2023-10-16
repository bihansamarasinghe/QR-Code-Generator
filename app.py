import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=1)

qr.add_data("https://github.com/bihansamarasinghe")

qr.make(fit=True)

img = qr.make_image()

img.save("mygithubprofile.jpeg")
