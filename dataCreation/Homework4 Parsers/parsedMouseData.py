f = open('mouselogs.txt','r')
output = open('../mouselogs_parse.txt','w')
for line in f:
    newLine = line.strip().split('-')
    
    time = float(newLine[0])
    position = newLine[1]
    button = int(newLine[2])
    color = ''
    
    position = position.split(',')
    pos_x = int(position[0])
    pos_y = int(position[1])
    if button == 513:
        color = "Red"
    elif button == 516:
        color = "Blue"
    else:
        color = "Green"
    
    output.write("{x:%.3f, y:%d, z:%d, fillColor:'%s'},\n" %(time, pos_y, pos_x, color) )
    
output.close()