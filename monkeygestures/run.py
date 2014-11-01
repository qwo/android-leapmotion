# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name

device.touch(100,500, 'DOWN')
device.touch(300,500, 'MOVE')
device.touch(300,400, 'MOVE')
device.touch(300,400, 'UP')

device.touch(100,500, 'RIGHT')
device.touch(100,500, 'RIGHT')
device.touch(100,500, 'RIGHT')
device.touch(100,500, 'RIGHT')

device.touch(300,400, 'UP')
device.touch(300,400, 'UP')
device.touch(100,800, 'UP')
device.touch(300,400, 'UP')
device.touch(300,400, 'UP')
device.touch(300,400, 'UP')
device.touch(300,400, 'UP')

device.drag((100,100),(100,400),0.15,8)
device.drag((100,100),(100,400),0.15,9)
device.drag((100,100),(100,400),0.15,5)

# package = 'com.google.android.youtube'
#
# # sets a variable with the name of an Activity in the package
# activity = 'com.google.android.youtube.MainActivity'
#

# Start the application
#device.startActivity (component = 'com.google.android.youtube / .MainActivity')

# # sets the name of the component to start
# runComponent = package + '/' + activity
#
# # Runs the component
# device.startActivity(component=runComponent)
#
# # Presses the Menu button
# device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
