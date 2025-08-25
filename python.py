import qrcode
data='www.keybr.com'
qr=qrcode.make(data)
qr.save("qrcode.png")
