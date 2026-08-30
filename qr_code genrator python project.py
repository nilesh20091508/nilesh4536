import qrcode

data = input("Enter the text or code data: ").strip()
filename = input("enter the filename (with .png): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_colour= "black", back_colour= "white")
image.save(filename)

print= (f" QRCode saved as {filename}")

