# Imports the monkeyrunner modules used by this program
print 'from relay_down'
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

device.wake()

device.drag((100,100),(100,400),0.15,5)
