import qrcode
from datetime import datetime
import streamlit as bel


def clean_text():
    bel.session_state['input'] = ''


bel.title('QRCode Generator Program')

data = bel.text_input("Plases enter your QR code data :", key='input')
data_placeholder = bel.empty()

if bel.button('Enter QR Code'):
    if data:
        img = qrcode.make(F'{data}')
        img_path = f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png"
        img.save(img_path)
        bel.image(img_path, width=300)
        bel.success("QRcode saved successfully")

        # clean_text()
        # bel.session_state['input'] = ''
        data_placeholder = bel.empty()
        # data = ''
        # bel.text_input("Please enter your QR code data :", value=data)

else:
    bel.warning("Plases enter your data before generator qrcode")
