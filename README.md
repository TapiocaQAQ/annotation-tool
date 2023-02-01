# Annotation Tool Usage

## Documents
> 1. Please `make sure that the data is in the right folder` and that `label.txt is changed`.

```
.
├─ input (Input files)
     ├─── source (you have to put video spurce here!)
     ├─── video (Extrated frames)
            └───── video_name/frame (run generate.py and auto generate frames.)
     ├─── frame.txt (URLID,Frame,Time)
     ├─── label.txt (TagID,Tag) (Have to write label you wnat to annotate!)
     └─── video.txt (URLID,URL)
├── lib (Web source code)
└── coin_annotation_tool.html (Click to label)
```


## Usage


### Load Files 

![](./images/load.png)

> 1. Click `coin_annotation_tool.html`

> 2. Click `Load video file`, `Load label file`, `Load frame file` to load `video.txt` ,`label.txt`, `frame.txt`

> 3. Click `Load` to load files 

![](./images/loaded.png)
---

### Start Labeling

#### Frame Mode

![](./images/FrameMode.jpeg)

> Operations

1. `Setting`: Set `Row`

2. `Save`: Save current results

3. `Delete`: Delete current video

> Usage

1. Select images by clicking start and end frame

2. Click and select `Tags`

3. Clear labeled results by `Clear`

---


## Download results

Click `Download` to download results 