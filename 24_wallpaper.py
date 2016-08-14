from PIL import Image
from datetime import datetime

hour = datetime.now().hour
img = Image.open('/home/shellshock/Pictures/ghost.jpg')
width = img.size[0]
heigth = img.size[1]
height_24 = (int(img.size[1]) - 600) / 24 * hour

img2 = img.crop((0,height_24,1024,600+height_24))
img2.save('/home/shellshock/Pictures/cron/_ghost.jpg')
