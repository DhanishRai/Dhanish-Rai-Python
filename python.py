import qrcode
data='www.keybr.com'
qr=qrcode.make(data)
qr.save("qrcode.png")
# this is just a fun time program