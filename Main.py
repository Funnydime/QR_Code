import qrcode
import qrcode.image.styles
import qrcode.image.styles.colormasks
import qrcode.image.styles.moduledrawers
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=1,
)

qr_data = input("Input what you want\n")

qr.add_data(f'{qr_data}')
qr.make(fit=True)

qr_color_1= input("This will be color 1\n")
qr_color_2= input("This will be color 2\n")

qr_color_1 = qr_color_1.lower()
qr_color_2 = qr_color_2.lower()

img = qr.make_image(fill_color=f"{qr_color_1}", back_color=f"{qr_color_2}")

qr_name = input("What is the name you want to save it as? \n")

img.save(f"{qr_name}.png")