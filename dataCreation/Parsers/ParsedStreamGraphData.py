#Requires GenerateAPMData.py to be run first

import os

dir = "../Data"

output = open("../StreamGraph/collectedAPMSeconds.csv", "w")

output.write("game,time,actions")

for folder in os.listdir(dir):
    filename = dir + "/" +  folder + "/Parsed Data/actionsPer10Second.csv"
    time = 0
    file  = open(filename, "r")
    for line in file:
        if line[0].isdigit():
            lineList = line.split(",")
            newTime = int(lineList[0])
            number = int(lineList[1])

            while( time+1 < newTime):
                time += 1
                output.write("\n%s,%d,%d" %(folder[4:], time, 0))

            time = newTime
            output.write("\n%s,%d,%d" %(folder[4:], time, number))

    while (time < 250):
        time += 1
        output.write("\n%s,%d,%d" %(folder[4:], time, 0))

    file.close()
output.close()