def convertLine(line):
    print("convert")
    lineDest = line.split(",")
    # print(lineDest)
    # print(len(lineDest))
    if len(lineDest) > 1:
        x1 = int(lineDest[0])
        y1 = int(lineDest[1])
        x2 = int(lineDest[2])
        y2 = int(lineDest[3])
        classe = int(lineDest[4])
        width = x2 - x1
        height = y2 - y1
        print(str(width) + "X" + str(height))
        centerX = float(x1 + width / 2)
        centerY = float(y1 + height / 2)
        # centerX = '{0:.6f}'.format(centerX)
        # centerY = '{0:.6f}'.format(centerY)
        res1 ='{0:.6f}'.format(centerX / 608)
        res2 ='{0:.6f}'.format(centerY / 608)
        res3 ='{0:.6f}'.format(width / 608)
        res4 ='{0:.6f}'.format(height / 608)

        return str(classe) + " " + str(res1)+" " + str(res2)+" " + str(res3)+" " + str(res4)+"\n"


file = open("final_train.csv", "r")

for line in file:
    print(line.split(" "))
    print(len(line.split(" ")))
    filename = line.split(" ")[0].replace(".jpg", ".txt")\
        .replace(".jpeg", ".txt")\
        .replace("patches/", "")\
        .replace(" ","")\
        .replace("\n", "")
    print('test '+filename)
    filename = filename.lstrip()
    print('test '+filename)
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    if len(filename) > 0:
        print(filename)
    if len(line.split(" ")) > 1:
        line1 = line.split(" ")[1]
        c1 = convertLine(line1)
    if len(line.split(" ")) > 2:
        line2 = line.split(" ")[2]
        c2 = convertLine(line2)
    if len(line.split(" ")) > 3:
        line3 = line.split(" ")[3]
        c3 = convertLine(line3)
    if len(line.split(" ")) > 4:
        line4 = line.split(" ")[4]
        c4 = convertLine(line4)
    if len(line.split(" ")) > 5:
        line5 = line.split(" ")[5]
        c5 = convertLine(line5)
    if len(line.split(" ")) > 6:
        line6 = line.split(" ")[6]
        c6 = convertLine(line6)








    f = open("yolov3/" +filename, "w")
    f = open("yolov3/" +filename, "a")
    if len(line.split(" ")) > 1:
        f.write(c1)
    if len(line.split(" ")) > 2:
        f.write(c2)
    if len(line.split(" ")) > 3:
        f.write(c3)
    if len(line.split(" ")) > 4:
        f.write(c4)
    if len(line.split(" ")) > 5:
        f.write(c5)
    if len(line.split(" ")) > 6:
        f.write(c6)
    f.close()
