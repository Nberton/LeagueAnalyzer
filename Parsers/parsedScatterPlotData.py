import os
from pynput import mouse

def ParseMouse(input, output):
    output.write("z,y,x,button")
    for line in input:
        newLine = line.strip().split('-')
        time = float(newLine[0])
        position = newLine[1].strip()
        button = newLine[2].strip()

        color = ''
        if button == "Button.right":
            color = 'right'
        elif button == "Button.left":
            color = 'left'
        else:
            color = 'green'

        position = position.split(',')
        pos_x = int(position[0])
        pos_y = int(position[1])

        #output.write('{"x":%.3f, "y":-%d, "z":-%d, "fillColor":"%s"}\n' % (time, pos_y, pos_x, color))
        output.write('\n%.3f,-%d,%d,%s' % (time, pos_y, pos_x, color))

def ParseGameFolder(gameFolder):
    mouseLogs = open(gameFolder + '/mouselogs.txt', 'r')
    mouseOutput = open(gameFolder + '/Parsed Data/mouseParse - Scatter.txt', 'w')
    ParseMouse(mouseLogs, mouseOutput)
    mouseLogs.close()
    mouseOutput.close()

    keyboardLogs = open(gameFolder + '/keylogs.txt', 'r')
    keyboardOutput = open(gameFolder + '/Parsed Data/keyboardParse - Scatter.txt', 'w')
    keyboardLogs.close()
    keyboardOutput.close()


if __name__ == '__main__':
    rootDir = '../Data'
    os.chdir(rootDir)

    for gameFolder in os.listdir('.'):

        ParseGameFolder(gameFolder)