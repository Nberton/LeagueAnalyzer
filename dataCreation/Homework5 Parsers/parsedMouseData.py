f = open('Game1/mouselogs.txt','r')
output = open('Game1/mouselogs_parse.txt','w')

count = 0
for line in f:
    line.replace(' ', '')
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
    
    if count == 0:
        output.write('{"x":%.3f, "y":-%d, "z":-%d, "fillColor":"%s"}' %(time, pos_y, pos_x, color) )
    else:
        output.write('\n{"x":%.3f, "y":-%d, "z":-%d, "fillColor":"%s"}' %(time, pos_y, pos_x, color) )
    count += 1
    
output.close()