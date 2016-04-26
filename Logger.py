from pynput import mouse
from pynput import keyboard
import pyaudio
import wave
import time
import os


CHUNK = 1024

def getFolder():
    gameNumber = 0
    for folder in os.listdir("Data/"):
        gameNumber += 1
    print gameNumber

    return gameNumber + 1


def Beep():
    wf = wave.open('../../beep.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()


def on_click_wait(x, y, button, pressed):
    if x == 0 and y == 0:
        Beep()
        return False


def on_click(x, y, button, pressed):




    if x == 0 and y == 0 and button == mouse.Button.left:
        Beep()
        Beep()
        keyboardListener.stop()
        return False

    currentTime = time.time() - start
    fp = open("mouselogs.txt", "a")

    fp.write("%.5f - %d,%d - %s\n" %(currentTime, x, y, button))
    # print "%.5f - %d,%d - %s" %(currentTime, x, y, button)
    fp.close()


def on_press(key):
    # if key == keyboard.Key.esc:
    #     return False

    currentTime = time.time() - start
    fp = open("keylogs.txt", "a")
    try:
        fp.write( "%.5f - %c\n" %(currentTime, key.char))
    except:
        fp.write("%.5f - %s\n" % (currentTime, key))

    # print key

    fp.close()


if __name__ == "__main__":
    gameNumber = getFolder()
    newFolder = "Data/Game%d" %gameNumber
    os.makedirs(newFolder)
    os.chdir(newFolder)
    readme = open("ReadMe.txt", "a")
    readme.close()
    os.mkdir('Parsed Data')


    # Collect events until released
    with mouse.Listener(on_click=on_click_wait) as listener:
        listener.join()

    start = time.time()
    with mouse.Listener(on_click=on_click) as mouseListener:
        with keyboard.Listener(on_press=on_press) as keyboardListener:
            keyboardListener.join()

        # keyboardListener.join()
        mouseListener.join()
