files = ["1", "2", "3", "4", "5"]

output = open("collectedAPM.csv", "w")

output.write("game,time,actions")

for folder in files:
    filename = "Game" + folder + "/actionsPerMinute.csv"
    time = 0
    file  = open(filename, "r")
    for line in file:
        if line[0].isdigit():
            lineList = line.split(",")
            newTime = int(lineList[0])
            number = int(lineList[1])
            
            while( time+1 < newTime):
                time += 1 
                output.write("\n%s,%d,%d" %(folder, time, 0))
                               
            time = newTime
            output.write("\n%s,%d,%d" %(folder, time, number))

    while (time < 50):
        time += 1
        output.write("\n%s,%d,%d" %(folder, time, 0))
        
    file.close()
output.close()