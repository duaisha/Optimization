from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import argparse
from pdf2image import convert_from_path

def convert_pdf2images(pdf_file, output_dir):
	i = 0
	pages = convert_from_path(pdf_file)
	for page in pages:
		page.save(output_dir + "/" + str(i) +'.png')
		i += 1

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pdf", type=str, default="",
	help="path to input video file")
ap.add_argument("-o", "--outdir", type=str, default="",
	help="path to output text file")
args = vars(ap.parse_args())

pdf_file = args["pdf"]
output_dir = args["outdir"]

convert_pdf2images(pdf_file, output_dir)






 




