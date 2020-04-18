import pyqrcode
from pyqrcode import QRCode
from PIL import Image

url = pyqrcode.QRCode('https://github.com/wut08?tab=repositories', error='H')
with open('test.png','wb') as f:
    url.png(f, scale=10)

img = Image.open('test.png')
img = img.convert("RGBA")
width, height = img.size
logo_size = 150
logo = Image.open('IMDB.jpg')

xmin = ymin = int((width/2) - (logo_size/2))
xmax = ymax = int((width/2)+(logo_size/2))

logo = logo.resize((xmax - xmin, ymax - ymin))

img.paste(logo, (xmin,ymin,xmax,ymax))
img.show()
img.save('MyGitHubQR.png')