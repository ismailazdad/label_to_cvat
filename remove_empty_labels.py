from os.path import join
from glob import glob
import os.path
from os import path

exist = 0
noexist = 0
files = []
pathImage = "/home/ismail/travail/algoscope/labels_to_cvat/"
os.chdir("/home/ismail/travail/algoscope/labels_to_cvat/")
for ext in ('*.jpeg', '*.jpg'):
    files.extend(glob(join("hematho_without_empty_label", ext)))

# print(files)

for file in files:
    print("#########################################")
    # print(file)
    fileText = file.replace(".jpg", ".txt").replace(".jpeg", ".txt")
    # print(pathImage+file)
    print(pathImage+fileText)
    print("file exist ? " + str(path.exists(pathImage+fileText)))
    print("file size  " + str(os.stat(pathImage+fileText).st_size))
    if path.exists(pathImage+fileText) and str(os.stat(pathImage+fileText).st_size) != "0":
        exist = exist + 1
    else:
        noexist = noexist + 1
        # f = open(fileText, "x")
        # print("create file "+fileText)
        os.remove(file)
        os.remove(pathImage+fileText)
        # f.close()
#
print('number file exist : ' + str(exist))
print('number file doesnt exist : ' + str(noexist) +' removed')
