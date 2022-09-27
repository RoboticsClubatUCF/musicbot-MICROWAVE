#import libraries
import time
from adafruit_servokit import ServoKit

#set channels for the ServoKit
kit = ServoKit(channels=16)

#all servos can be rotated 180 degrees, the min and max, also known as the on and off states of the servos is written below :

off = 90
on = 170


