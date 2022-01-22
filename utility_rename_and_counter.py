"""""
************************
** Here's the problem **
************************

A friend built a church made of Lego and the result was impressive!
So, we decided to take 78 photos rotating the model of some degrees each time to obtain like a "3D model" (I'm a 3D-things profane).
I discovered this open-source library: https://scaleflex.github.io/js-cloudimage-360-view/ that made all the dirty work.

But there was a problem: I needed to rename 78 photos with these filenames

images
├── DSC_0103.jpg
├── DSC_0104.jpg
├── DSC_0105.jpg
├── DSC_0106.jpg
└── DSC_0107.jpg

to these (where the counter will be used by the library to make the magic).

images
├── img-1.jpg
├── img-2.jpg
├── img-3.jpg
├── img-4.jpg
└── img-5.jpg

Here, a little Python script to solve the boring problem.

""""

import os

path = "./images/"

images = os.listdir(path) # get the list of images

i = 1 # counter
for img in images :
    os.rename(os.path.join(path,img), os.path.join(path, "img-" + str(i) + ".jpg")) # the library doesn't need a specific filename, but I chose img-X.jpg
    i += 1