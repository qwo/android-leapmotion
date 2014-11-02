# Imports the monkeyrunner modules used by this program
print 'from relay_left'

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

device.wake()

# drag (tuple start, tuple end, float duration, integer steps)

# Left drag
device.drag((400,100),(100,100),0.15,5)
