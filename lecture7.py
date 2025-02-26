import qrcode
img = qrcode.make("https://www.linkedin.com/in/syed-ghulam-mustafa-b1b0a434a/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app") #yahan inverted commas k andar kuch bhi likh do uska qr code bn jayga
print(type(img))
img.save("syed-ghulam-mustafa-linkedin.png")
print('QR Code Generated')