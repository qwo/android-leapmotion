#!/usr/bin/env monkeyrunner

import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

# Touch down screen
device.touch(100, 500, MonkeyDevice.DOWN)

# A swipe left from (x1, y) to (x2, y) in 2 steps
center = 400 #center
x1 = 100#left
x2 = 400#right
y2 = 600#up
y3 = 200#down

startfromleft = (x1, center)
endfromright = (x2, center)

duration = 0.2
steps = 2
pause = 0.2

for i in range(1, 250):
    # Every so often inject a touch to spice things up!
    if i % 9 == 0:
        device.touch(x2, center, 'UP_AND_DOWN')
        MonkeyRunner.sleep(pause)
    # Swipe right
    device.drag(start, end, duration, steps)
    MonkeyRunner.sleep(pause)
    # Swipe left
    device.drag(end, start, duration, steps)
    MonkeyRunner.sleep(pause)

    # Swipe up
    device.drag(end, start, duration, steps)
    MonkeyRunner.sleep(pause)

device.drag((100,100),(100,400),0.15,8)
