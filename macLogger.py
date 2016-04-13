from pynput import mouse
from pynput import keyboard
import pyaudio
import wave
import time


CHUNK = 1024

def Beep():
    wf = wave.open('beep.wav', 'rb')
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
    if x == 0 and y == 0:
        Beep()
        keyboardListener.stop()
        return False

    currentTime = time.time() - start

    print "%.5f - %d,%d" %(currentTime, x, y)


def on_press(key):

    if key == keyboard.Key.esc:
        return False

    currentTime = time.time() - start

    print "%.5f - %s" % (currentTime, key)


# Collect events until released
with mouse.Listener(on_click=on_click_wait) as listener:
    listener.join()


start = time.time()

with mouse.Listener(on_click=on_click) as mouseListener:

    with keyboard.Listener(on_press=on_press) as keyboardListener:
        keyboardListener.join()

    # keyboardListener.join()
    mouseListener.join()




