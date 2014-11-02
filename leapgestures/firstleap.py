import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = './x64'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

import subprocess
from subprocess import call

class FirstListenerInline(Leap.Listener):
    gesture_by_finger = {}

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_frame(self, controller):
        frame = controller.frame()
        all_gestures = frame.gestures()

        if(len(all_gestures) > 0):
            # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
            for gesture in all_gestures:
                swipe_gesture_obj = Leap.SwipeGesture(gesture);
                if len(self.gesture_by_finger) < 1:
                    print "INITIALIZING"
                if str(swipe_gesture_obj.pointable.id) in self.gesture_by_finger:
                    self.gesture_by_finger.get(str(swipe_gesture_obj.pointable.id)).append(swipe_gesture_obj)
                else:
                    self.gesture_by_finger.update({str(swipe_gesture_obj.pointable.id) : []})
                # print swipe_gesture_obj.direction, swipe_gesture_obj.pointable;
        else:
            if len(self.gesture_by_finger) > 0:
                print "No gesture. Findin movement."
                mmt_name = self.find_movement(self.gesture_by_finger)
                self.gesture_by_finger = {}
                print "ERASED"
                name =  os.path.abspath('relay_'+mmt_name+'.py')
                print name
                x = call(['C:\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\monkeyrunner.bat', name])
                x.stdin.write('\n')

    def find_movement(self, gestures):
        print "Got gestures: ", len(gestures)
        working_limb = -1
        max_events = 0
        for k,v in gestures.items():
            # print k, v
            if len(v) > max_events:
                max_events = len(v)
                working_limb = k

        working_gesture_set = gestures.get(working_limb)
        # print "Working Finger:", working_limb, ", #Events:", max_events
        # print type(working_gesture_set[0]), type(working_gesture_set[1])

        starting_coords = working_gesture_set[0].direction
        ending_coords = working_gesture_set[len(working_gesture_set)-1].direction
        print "S", starting_coords, "E", ending_coords
        endx = ending_coords[0]
        endy = ending_coords[1]
        # FORWARD: 0, BACKWARD: 1, UPWARD: 2, DOWNWARD: 3
        if endx >= 0 and endy >= 0:
            if abs(endx) > abs(endy):
                print "FORWARD"
                return 'right'
            else:
                print "UPWARD"
                return 'top'
        elif endx < 0 and endy <0:
            if abs(endx) > abs(endy):
                print "BACKWARD"
                return 'left'
            else:
                print "DOWNWARD"
                return 'down'
        elif endx < 0 and endy > 0:
            if abs(endx) > abs(endy):
                print "BACKWARD"
                return 'left'
            else:
                print "UPWARD"
                return 'top'
        elif endx > 0 and endy < 0:
            if abs(endx) > abs(endy):
                print "FORWARD"
                return 'right'
            else:
                print "DOWNWARD"
                return 'down'

def main():
    # Create a sample listener and controller
    listener = FirstListenerInline()
    controller = Leap.Controller()
    controller.config.set("Gesture.Swipe.MinLength", 100.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 750)
    controller.config.save()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
