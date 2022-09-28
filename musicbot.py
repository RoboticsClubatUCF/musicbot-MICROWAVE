# import libraries
import time

from adafruit_servokit import ServoKit
from midi import *
from songChoice import *

# set channels for the ServoKit
kit = ServoKit(channels=16)

# all servos can be rotated 180 degrees, the min and max, also known as the on and off states of the servos is written below :

off = 90
on = 80 # this is the distance the servo has to spin to be in the on position

midiR = MidiReader(get_song_request().dir)


# we have 13 "keys" we can press at once, so we will calculate the max and min notes, and subtract by the min to find my range, and thus know which notes need to be struck
print("Song Selected Has Range : ",midiR.range)
if (midiR.range) > 13:
    print("SONG CANNOT BE PLAYED!!! \nSONG REQUIRES ",{midiR.range}, " NOTES OF RANGE, AND WE HAVE 13!!!")
    exit(1)

def play_song():
    for msg in midiR.messages:
        kit.servo[msg.note - midiR.min].angle = (off) + (msg.on * on) # this is cursed
        time.sleep(msg.time)


