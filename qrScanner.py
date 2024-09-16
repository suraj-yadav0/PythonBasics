import qrcode

myqr = qrcode.make("www.google.com")
myqr.save("google.png")