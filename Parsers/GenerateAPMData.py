import os


def CollectAPM(folder):
    mouse = open(folder + '/mouselogs.txt', 'r')
    keyboard = open(folder + '/keylogs.txt', 'r')
    output = open(folder + '/Parsed Data/actionsPer10Second.csv', 'w')

    actions = {}

    for line in mouse:
        line.replace(' ', '')
        newLine = line.strip().split('-')

        time = int(float(newLine[0])) / 10
        if time in actions:
            actions[time] += 1
        else:
            actions[time] = 1

    for line in keyboard:
        line.replace(' ', '')
        newLine = line.strip().split('-')

        time = int(float(newLine[0])) / 10
        # print time
        if time in actions:
            actions[time] += 1
        else:
            actions[time] = 1

    output.write("time,actions")
    for item in actions:
        output.write("\n%d,%d" % (item, actions[item]))
        # print item, ":", actions[item]

    output.close()
    mouse.close()
    keyboard.close()


if __name__ == '__main__':
    rootDir = '../Data'
    os.chdir(rootDir)

    for gameFolder in os.listdir('.'):
        print gameFolder
        CollectAPM(gameFolder)


