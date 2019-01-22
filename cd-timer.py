#Orig code: https://www.daniweb.com/programming/software-development/threads/464062/countdown-clock-with-python
#coundown timer, without annoying blinky cursor - Ponzi

import time
import subprocess
import curses
import sys

print("Coundown timer, input time in seconds.\nExample: 900 seconds = 15 min.")

theTime = int(input("Input coundown time: "))
stdscr = curses.initscr()
curses.curs_set(0)

for t in range(theTime, -1, -1):
    try:
        minutes = t / 60
        seconds = t % 60
        print("%d:%2d" % (minutes,seconds), end='\r')
        time.sleep(1.0)
    except KeyboardInterrupt:
        curses.curs_set(1)
        sys.exit()
        if minutes == 0 and seconds == 0:
            print("Timed out.")
            for x in range(3):
                subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'system-ready'])

curses.curs_set(1)


