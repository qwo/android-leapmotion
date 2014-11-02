# Imports the monkeyrunner modules used by this program
print 'from relay_left'

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object

# drag (tuple start, tuple end, float duration, integer steps)

# Left drag


# Echo server program
import socket


print 'main invoked'
HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print 'server setup complete'

device = MonkeyRunner.waitForConnection()
device.wake()

print 'MonkeyRunner server running...'

conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    if(data == '0'):
        print 'left'
    elif (data == '1'):
        print 'right'
    elif (data == '2'):
        print 'up'
    elif (data == '3'):
        print 'down'
    else:
        print 'did not understand this: ', data

    # conn.sendall(data)
conn.close()

# if '__name__' == '__main__':
#     main()
