# LeagueAnalyzer

Python version : 2.7.11

To get macLogger.py running on mac via terminal
```sh
$ brew install python
$ brew install portaudio
$ pip install pynput
$ pip install pyaudio
```

When recording on Mac, you must grant accessibility to League
* Settings
* Security and Privacy
* Privacy
* Accessibility
* click the "+" (If this is disabled you need to click the lock in the bottom left)
* Find League of Legends under applications
* Click "Open" to add it

Steps when using the program:
* Open LoL and macLogger.py
* Run MacLogger.py and begin League game
* Once you have entered the game left click in the top left corner (pixel 0,0)
   and there should be an audible "Beep" signaling that the program
   begun recording mouse/keyboard input.
* Win or Lose
* At the end of the match left click the top left corner again
   to end the program.  There should be an audible "Beep" signaling
   the program has ended.
* Create a ReadMe to record the champion and lane position.
