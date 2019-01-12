from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import cv2

def get_watermarkImage(image, roll_no):
	
	originalImage = Image.open(image).convert("RGB")
	width, height = originalImage.size

	x = np.asarray(originalImage).shape 


	if(len(x) == 3): 
		t = 'RGB'
	else:		
		t = 'L'
	
	
	imgWatermark = Image.new(t, (2*width, 2*height), color = "white") 
	widthNew, heightNew = imgWatermark.size
	draw = ImageDraw.Draw(imgWatermark)

	font = ImageFont.truetype('Arial.ttf', 60)
	textwidth, textheight = draw.textsize(roll_no, font)

	x = 0
	y = 0

	for i in range(10):
		x += 600
		y =0
		for j in range(10):
			y += 400
			draw.text((x,y), roll_no, font=font, fill= 100)
	rot = imgWatermark.rotate(45,expand=0)
	
	right = (width/2) + (width)
	lower = (height/2) + (height)

	box = (int(width/2), int(height/2), int(right), int(lower))#######################################3
	watermarkImage = rot.crop(box)
	#originalImage.show()
	#cropped_img.save('watermark.png')
	#print(watermarkImage, originalImage)
	res = Image.blend(originalImage, watermarkImage, alpha =0.2)
	return res



image = 'output-0.png'
roll_no = '12345677777'
img_watermark = get_watermarkImage(image, roll_no)
img_watermark.save('watermark.png')

#d = os.listdir("../5/")
#for i in range(len(d)):
#	image = d[i]
#	roll_no = '12345677777'
#	print(i, image)
#	img_watermark = get_watermarkImage("../5/"+image, roll_no)
#	img_watermark.save('watermark_'+image[:-4]+'.png')






 




