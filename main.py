import qrcode as qr
img = qr.make("https://www.linkedin.com/in/abhishek-s-gupta")
img.save("linkedin_qr.png")