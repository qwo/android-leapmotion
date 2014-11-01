# Imports the monkeyrunner modules used by this program


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name

#Controller for MotoG


#! /usr/bin/env monkeyrunner

# import the MonkeyRunners modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

def startbrowser(d):
	d.broadcastIntent("http://www.google.com/", "ACTION_MAIN")
	d.startActivity(component="com.android.browser/.BrowserActivity")

def main():
   	print "Start"
	# Connect to the current device returning the MonkeyDevice object

    #MonkeyRunner.alert("Starting Activity", "monkeyrunner", "OK")

if not device:
    print "Couldn't get connection"
    sys.exit()

    print "Found device"
    startBrowser(device)
    MonkeyRunner.sleep(10.0)

main()
# package = 'com.google.android.youtube'
#
# # sets a variable with the name of an Activity in the package
# activity = 'com.google.android.youtube.MainActivity'
#

#Start the application
device.startActivity (component = 'com.google.android.youtube / .MainActivity')

# sets the name of the component to start
runComponent = package + '/' + activity
#
# Runs the component
device.startActivity(component=runComponent)
