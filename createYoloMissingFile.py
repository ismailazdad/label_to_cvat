from os.path import join
from glob import glob
import os.path
from os import path

exist = 0
noexist = 0
files = []
pathImage = "/home/ismail/travail/algoscope/labels_to_cvat/"
for ext in ('*.jpeg', '*.jpg'):
    files.extend(glob(join("yolov3", ext)))

print(files)

for file in files:
    print("#########################################")
    # print(file)
    fileText = file.replace(".jpg", ".txt").replace(".jpeg", ".txt")
    # print(pathImage+file)
    print(pathImage+fileText)
    # print("file exist ? " + str(path.exists(pathImage+fileText)))
    if path.exists(pathImage+fileText):
        exist = exist + 1
    else:
        noexist = noexist + 1
        # f = open(fileText, "x")
        # print("create file "+fileText)
        os.remove(file)
        # f.close()
#
print('number file exist : ' + str(exist))
print('number file doesnt exist : ' + str(noexist) +' removed')
