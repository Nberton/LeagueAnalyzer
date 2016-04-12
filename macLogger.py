from pynput.mouse import Listener
import pyaudio
import wave


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


def on_click(x, y, button, pressed):
    if x == 0 and y == 0:
        Beep()
        return False
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False
    if pressed:
        Beep()


# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()