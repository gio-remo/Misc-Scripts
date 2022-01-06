"""""
************************
** Here's the problem **
************************

When developing a Veeva iDetail for Loud (@ Milan, Italy) I receive the asset images in a folder like this:

exported_images/
├── slide-01/
│   ├── slide01-bg.jpg
│   ├── slide01-full.jpg
│   └── slide01-thumb.jpg
└── slide-02/
    ├── slide02-bg.jpg
    ├── slide02-full.jpg
    ├── slide02-thumb.jpg
    ├── pop10.png
    └── other.png

Usually, an iDetail consists of 30 slides but sometimes, it can reach also 50/60 slides.
Every slide has a background (*bg.jpg), two previews, the bigger (*full.jpg) and the smaller (*thumb.jpg), and other assets such as the images for the popups or the scroll.

What I need to do is to have a folder like this:

idetail_X/
├── 01_idetail_X/
│   ├── images/
│   │   └── slide/
│   │       └── slide.jpg       (*bg.jpg)
│   ├── 01_idetail_X-full.jpg   (*full.jpg)
│   └── 01_idetail_X-thumb.jpg  (*thumb.jpg)
└── 02_idetail_X/
    ├── images/
    │   ├── slide/
    │   │   └── slide.jpg
    │   ├── pop10.png           (other)
    │   └── other.png           (other)
    ├── 02_idetail_X-full.jpg
    └── 02_idetail_X-thumb.jpg

*bg.jpg         => becomes /images/slide/slide.jpg
*full.jpg       => becomes slidename-full.jpg
*thumb.jpg      => becomes slidename-thumb.jpg
everything else => goes in /images/

What I used to do was to MANUALLY move each image in the respective destination folder, and then renaming it.
I can easily confirm that it was an extremely boring and time consuming task.

So, here the script that I run when ordering the files for the development of a Veeva iDetail.

"""""

import os
import shutil
import glob

pathSlides = "./img/" # ./exported_images/
slides = os.listdir(pathSlides)

pathDest = [
    "01_idetail_X",
    "02_idetail_X"
]

i = 0
for f in pathDest :

    # At first, I move ALL the images in the /images/ folder of the destination
    pathImages = pathSlides + slides[i] + "/*"
    images = glob.glob(pathImages)
    print(images)
    for img in images :
        temp = f + "/images/" + os.path.basename(img)
        shutil.copy(img, temp)

    # Then, I move and rename the FULL (deleting the copy)
    pathF = f + "/images/*full.jpg"
    full = glob.glob(pathF)
    temp = f + "/" + f + "-full.jpg"
    shutil.copy(full[0], temp)
    os.remove(full[0])

    # Then, I move and rename the THUMB (deleting the copy)
    pathT = f + "/images/*thumb.jpg"
    thumb = glob.glob(pathT)
    temp = f + "/" + f + "-thumb.jpg"
    shutil.copy(thumb[0], temp)
    os.remove(thumb[0])
    
    # Then, I move and rename the BG (deleting the copy)
    pathB = f + "/images/*bg.jpg"
    bg = glob.glob(pathB)
    temp = f + "/images/slides/slide.jpg"
    shutil.copy(bg[0], temp)
    os.remove(bg[0])

    i += 1
