# making a qr code using python
import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=EH9yR6T4ePI")
img.save("ay meri meri zoharajabi.png")