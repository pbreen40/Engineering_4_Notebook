import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24 
accelerometer = Adafruit_LSM303.LSM303() # setting up accelerometer
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) # setting up display
disp.begin() #starting display, clearing display
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) 
draw.rectangle((0,0,width,height), outline=0, fill=0) # clears screen


padding = 3
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default() 



while True:   
	accel, mag = accelerometer.read() # gathers accelerometer data
	accel_x, accel_y, accel_z = accel 
	
	

	draw.text((x, top), "Accelerometer Data:", font=font, fill=255) 
	draw.text((x, top + 10), "Accel x ={0}".format(round(accel_x / 100, 3)), font=font, fill=255) # prints x 
	draw.text((x, top + 20), "Accel y ={0}".format(round(accel_y / 100, 3)), font=font, fill=255) # prints y
	draw.text((x, top + 30), "Accel z ={0}".format(round(accel_z / 100, 3)), font=font, fill=255) # prints z
	
	
	disp.image(image) 
	disp.display()

	
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0) 
	disp.image(image)
	disp.display()

	#sleep for debug, I've found it to be useful in the past
	time.sleep(.15)
