import os
import cv2
from pathlib import Path
from tqdm import tqdm
from optparse import OptionParser


parser = OptionParser()


parser.add_option("-i", "--interval", dest="interval", default=5,
                  help="how many frame you want to skip.                    EX: 30 fps with 5 interval and you will got 6 frames in 1s")


(options, args) = parser.parse_args()


## init txt
video_list = os.listdir(path='./input/source')
# init video.txt
f = open('./input/video.txt','w')
f.write("URLID,URL\n")
for ele in video_list:
    f.write(f"{ele.split('.')[0]},{ele}\n")
f.close()

# init frame.txt
f = open('./input/frame.txt','w')
f.write("URLID,Frame,Time\n")
f.close()


for video_name in video_list:

    frame_index = 0  # original video frame
    frame_count = 0  # save frame count
    interval = options.interval  #
    frame_list = []

    video = cv2.VideoCapture(f'./input/source/{video_name}')
    fps = video.get(cv2.CAP_PROP_FPS)
    print(fps)
    
    video_root = Path(f"./input/video/")
    video_root.mkdir(exist_ok=True)

    frame_root = Path(f"./input/video/{video_name.split('.')[0]}")
    print(frame_root)
    frame_root.mkdir(exist_ok=True)

    success = True if video.isOpened() else  False
    if not success:
        print("Read Video Fail")
    with tqdm(total=frame_index+1) as pbar:
        while(success):
            success, frame = video.read()
            if not success:
                print(f"finish {video_name}\n---------------------------------------------------------")
                break
            #print(f'read {frame_index} frames')
            if frame_index % interval == 0:
                img_name = f'{str(frame_count).zfill(5)}.jpg'
                cv2.imwrite(f"{frame_root}/{img_name}", frame)
                frame_list.append(f"{video_name.split('.')[0]},{img_name},{(frame_index/fps):.2f}")
                frame_count += 1
            frame_index += 1
            pbar.update(1)
    f = open('./input/frame.txt','a')
    for ele in frame_list:
        f.write(ele+'\n')
    f.close()
