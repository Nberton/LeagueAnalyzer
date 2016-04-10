f = open('keylogs.txt','r')
output = open('keylogs_parse.txt','w')
for line in f:
    newLine = line.strip().split('-')
    
    time = float(newLine[0])
    char = newLine[1]
    ascii = int(newLine[2])
    
    output.write("%.3f,%s,%d\n" %(time, char, ascii) )
    
output.close()