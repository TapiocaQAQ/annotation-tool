import os
import cv2
from pathlib import Path
from tqdm import tqdm
from optparse import OptionParser


parser = OptionParser()


parser.add_option("-i", "--interval", dest="interval", default=5,
                  help="how many frame you want to skip.                    EX: 30 fps with 5 interval and you will got 6 frames in 1s")


(options, args) = parser.parse_args()
print(options.interval)