"""
pyinstaller --onefile --icon=icon.ico merge_image.py --hidden-import=queue
"""
# -*- coding: utf-8 -*-

from natsort import natsorted
from PIL import Image
import msvcrt
import getopt
import glob
import sys


def merge_image(images_path, png=False):
	try:
		image_extension = '.jpg'
		image_type = 'JPEG'

		if png:
			image_extension = '.png'
			image_type = 'PNG'

		print("[INFO] sorting images...")
		images = natsorted([i.replace('\\', '/') for i in glob.glob(images_path + '/*.*')])  # get a list of images

		print("[INFO] measuring image dimensions...")
		XY_value_list = [[Image.open(file).size[0], Image.open(file).size[1]] for file in images]  # get the dimension of all the images
		height = int(sum([y for (x, y) in XY_value_list]))

		if height > 65530:
			image_extension = '.png'
			image_type = 'PNG'

		print("[INFO] creating stitched image...")
		# prepare a empty canvas (may take a lot of space of the memory)
		img_final = Image.new('RGB', (max([x for (x, y) in XY_value_list]), height), "white")

		y_offset = 0  # y offset changes to paste the image at the right place

		print("[INFO] stitching...")
		# loop all images
		for i in range(len(images)):
			img_final.paste(Image.open(images[i]), (0, y_offset))  # paste image...
			y_offset += XY_value_list[i][1]  # and increase y offset!

		print("[INFO] saving image...")
		img_final.save(images_path + "/" + images_path + " merged" + image_extension, image_type, quality=100)  # save image as a file

		# import shutil
		# shutil.rmtree(images_path, ignore_errors=True)  # remove fragmented images
		return True

	except Exception as err:
		print("[ERROR] while merging image:", err)
		return False


def usage():
	print('=====================================================')
	print('usage: merge_image.exe <folder name>')
	# options
	print('\t example: python merge_image.py -p -d <folder name>')
	print('\t example: merge_image.exe -p -d <folder name>')
	print('=====================================================')

	input("Press Enter to exit...")
	sys.exit(1)


if __name__ == '__main__':
	print("[INFO] initiating program...")
	images_folder = ""
	output_folder = ""
	save_as_png = False

	try:
		options, arguments = getopt.getopt(sys.argv[1:], "hpd:", ["help", "png", "directory="])

	except getopt.GetoptError as err:
		print("[ERROR]:", err)
		usage()
		print("press any key to exit...")
		msvcrt.getch()
		sys.exit(-1)

	for option, argument in options:
		if (option == "-p") or (option == "--png"):
			save_as_png = True

		elif (option == "-d") or (option == "--directory"):
			images_folder = argument

			if images_folder[-1] in ("\\", "/"):
				images_folder = images_folder[:-1]

		elif (option == "-h") or (option == "--help"):
			usage()

	if images_folder is None:
		print("[ERROR]: you didn't give the folder name")
		usage()
		print("press any key to exit...")
		msvcrt.getch()
		sys.exit(-1)

	merge_image(images_folder, save_as_png)
	print('[INFO] exit program')
	sys.exit(0)
