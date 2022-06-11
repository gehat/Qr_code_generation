import qrcode
import cv2
import yadisk


y = yadisk.YaDisk(token="AQAAAAAzOwnEAAf56nUrxnY-s0QdhKan9z7tgzE")
#Генерация QR по ссылке
def qrsearch(name, urls):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(urls)
    qr.make(fit=True)

    img = qr.make_image(fil_color='black', back_color='white')
    img.save('qr_codes.jpg', 'jpeg')
    y.upload('qr_codes.jpg', f'/Полка/QR-codes/{name}.jpeg')