import qrcode
from datetime import datetime

print('QRCode Generator Program')
print('Please type Exit')

while True:
    data = input('Please enter your QRCode data :')
    if data == 'Exit':
        break
    else:
        img = qrcode.make(F'{data}')
        type(img)  # qrcode.image.pil.PilImage
        img.save(f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png")
        print("QRCode image saved")
