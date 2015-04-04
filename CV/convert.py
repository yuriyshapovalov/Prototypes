#!/usr/bin/env python
from PIL import Image
import os, sys

def main(infile):
    image_folder = 'images/'
    pil_im = Image.open(image_folder + infile)
    pil_im.thumbnail((120, 120)).save(image_folder + "new_" + infile)

if __name__ == '__main__':
    main(str(sys.argv[1]))