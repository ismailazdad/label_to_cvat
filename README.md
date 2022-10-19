# label_to_cvat

**labels_to_cvat.py**

generate a zip files compatible with [cvat](https://github.com/opencv/cvat)

#example :

labels_to_cvat.py -f test2 -c RBC,WBC,Platelets 


labels_to_cvat.py -f repo -c classeNames

**generate_images.py**

get a list of images and generate randomly effect on the images (brightness,crop,rotate...)

**yolov3tov5.py**

wait for csv yolov3 file(final_train.csv) and generate a repo file compatible for yolov5

**autosplit.py**

make repartition assets to group train val and test repo , and create 3 files containing the assets repartition

autosplit_train.txt, autosplit_val.txt, autosplit_test.txt

example :

param : path to the images and proportion wanted between train , val and test

!python autosplit.py autosplit '../hemato/train/images' 0.9 0.05 0.05

will generate files containing the proportion

be ware remember to change your classes.yaml with the path of the new files instead the repository directly

train: ../hemato/train/autosplit_train.txt

val: ../hemato/train/autosplit_val.txt

test: ../hemato/train/autosplit_test.txt







 
 
