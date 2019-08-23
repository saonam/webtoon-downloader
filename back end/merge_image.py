# -*- coding: utf-8 -*-
"""
This script merges image into one file and save it in one higher level of folder

pyinstaller --onefile --icon=icon.ico merge_image.py --hidden-import=queue
"""

from natsort import natsorted
from PIL import Image
import shutil
import getopt
import glob
import sys


def merge_image(images_path, png=True, remove_after_merge=False):
    try:
        image_extension = '.jpg'
        image_type = 'JPEG'
        
        if png:
            image_extension = '.png'
            image_type = 'PNG'
        
        print("[INFO] sorting images...")
        images = natsorted(glob.glob(images_path + '/*.*'))  # get a list of images
        
        print("[INFO] measuring image dimensions...")
        XY_value_list = [[Image.open(file).size[0], Image.open(file).size[1]] for file in images]  # get the dimension of all the images
        height = int(sum([y for (x, y) in XY_value_list]))
        
        if height > 65530:  # maximum height of jpg image
            image_extension = '.png'
            image_type = 'PNG'
        
        print("[INFO] creating stitched image...")
        # prepare a empty canvas (may take a lot of space of the memory)
        img_final = Image.new('RGB', (max([x for (x, y) in XY_value_list]), height), "white")
        
        y_offset = 0
        
        print("[INFO] stitching...")
        # loop all images
        for i in range(len(images)):
            img_final.paste(Image.open(images[i]), (0, y_offset))  # paste image...
            y_offset += XY_value_list[i][1]  # and increase y offset!
        
        print("[INFO] saving image...")
        if True:
            img_final.save(images_path.split("/")[-1] + " merged" + image_extension, image_type, quality=100)
        
        shutil.rmtree(images_path, ignore_errors=True)
        return True
    
    except Exception as err:
        print("[ERROR] while merging image:", err)
        return False


def usage():
    print('=====================================================')
    print('usage: merge_image.exe -d <folder name>')
    print("help:  merge_image.exe -h")
    print('=====================================================')
    
    input("Press Enter to exit...")
    sys.exit(1)


if __name__ == '__main__':
    print("[INFO] initiating program...")
    images_folder = None
    output_folder = None
    
    try:
        options, arguments = getopt.getopt(sys.argv[1:], "hd:", ["help", "directory="])
    
    except getopt.GetoptError as err:
        print("[ERROR]:", err)
        usage()
        input("press Enter to exit...")
        sys.exit(-1)
    
    for option, argument in options:
        if (option == "-d") or (option == "--directory"):
            images_folder = str(argument)
            
            if "\\" in images_folder:
                images_folder = images_folder.replace("\\", "/")
            
            if images_folder[-1] == "/":
                images_folder = images_folder[:-1]
            
            print("[INFO] merging: " + images_folder)
        elif (option == "-h") or (option == "--help"):
            usage()
    
    if images_folder is None:
        print("[ERROR]: you didn't give the folder name")
        usage()
        input("press Enter to exit...")
        sys.exit(-1)
    
    merge_image(images_folder)
    print('[INFO] done!\n')
    sys.exit(0)
