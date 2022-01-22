"""""
************************
** Here's the problem **
************************

When developing Veeva iDetail, one day I had to export a new version of the images that were already structured like this:

slide-01/
├── img
└── img
slide-02/
├── img
└── img
slide-03/
├── img
└── img

My task was to export from InDesign the new versions of the images, but first I needed to empty the folders WITHOUT deleting everything and creating again all the structure.
My goal was to have just empty folders:

.
├── slide-01
├── slide-02
└── slide-03

Here the small script to solve this problem.

""""

import os
import shutil
import glob

slides = os.listdir(".") # make a list of the current folders

for s in slides:
    
    path = s + "/*" # with * I select everything inside
    images = glob.glob(path) # list of the content of the folder

    for i in images:
        os.remove(i)