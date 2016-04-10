mouse = open('Game4/mouselogs.txt','r')
keyboard = open('Game4/keylogs.txt', 'r')
output = open('Game4/actionsPerMinute.csv','w')

actions = {}

for line in mouse:
    line.replace(' ', '')
    newLine = line.strip().split('-')
    
    time = int(float(newLine[0]))/60
    if time in actions:
        actions[time] += 1
    else:
        actions[time] = 1
        
for line in keyboard:
    line.replace(' ', '')
    newLine = line.strip().split('-')
    
    time = int(float(newLine[0]))/60
    #print time
    if time in actions:
        actions[time] += 1
    else:
        actions[time] = 1    
    

output.write("time,actions")
for item in actions:
    output.write("\n%d,%d" %(item, actions[item]) )
    #print item, ":", actions[item]
    
output.close()
    