#!/usr/bin/python

import os,sys
import RPi.GPIO as GPIO
import time

adafruit_path = os.path.abspath('Adafruit_PWM_Servo_Driver')
sys.path.append(adafruit_path)

spacebrew_path = os.path.abspath('spacebrewInterface')
sys.path.append(spacebrew_path)

from Adafruit_PWM_Servo_Driver import PWM
from spacebrew import Spacebrew

arrSwitchVals = [-1, -1, -1, -1]
arrSwitchPins = [18, 23, 24, 25]

#OUTPUT PINS FOR THE RELAY
GPIO.setmode(GPIO.BCM)
for i in range(0,3):
  GPIO.setup(arrSwitchPins[i], GPIO.OUT)

# ===========================
# CREATE SPACEBREW AND SUBSCRIBE
# =========================

brew_array = Spacebrew("rpi_servo_array",server="10.70.2.124")

#CREATE SUBSCRIBERS
brew_array.addSubscriber("servo0_cam_pan","range")
brew_array.addSubscriber("servo1_cam_tilt","range")
brew_array.addSubscriber("servo2","range")
brew_array.addSubscriber("servo3","range")
brew_array.addSubscriber("servo4","range")
brew_array.addSubscriber("servo5","range")
brew_array.addSubscriber("servo6","range")
brew_array.addSubscriber("servo7","range")
brew_array.addSubscriber("servo8","range")
brew_array.addSubscriber("servo9","range")
brew_array.addSubscriber("servo10","range")

brew_array.addSubscriber("relay1_ac", "boolean")
brew_array.addSubscriber("relay2_ac", "boolean")
brew_array.addSubscriber("relay3_dc", "boolean")
brew_array.addSubscriber("relay4_dc", "boolean")

brew_array.addPublisher("relay1_ac", "boolean")
brew_array.addPublisher("relay2_ac", "boolean")
brew_array.addPublisher("relay3_dc", "boolean")
brew_array.addPublisher("relay4_dc", "boolean")


# =========================
# SPACEBREW EVENT HANDLERS
# =========================

# SERVOS
def servo_all(servoNum, tVal):

  val = servoMin + (450*tVal)/1023
  pwm.setPWM(servoNum, 0, val)
  print "servo",servoNum,":",value

def servo0(value):
  servo_all(0,value)
def servo1(value):
  servo_all(1,value)
def servo2(value):
  servo_all(2,value)
def servo3(value):
  servo_all(3,value)
def servo4(value):
  servo_all(4,value)
def servo5(value):
  servo_all(5,value)
def servo6(value):
  servo_all(6,value)
def servo7(value):
  servo_all(7,value)
def servo8(value):
  servo_all(8,value)
def servo9(value):
  servo_all(9,value)

# SWITCHES
def switch_all(switchNum,tVal):

  global arrSwitchVals
  global arrSwitchPins

  tVal = arrSwitchVals[switchNum]
  tPin = arrSwitchPins[switchNum]

  arrSwitchVals[switchNum] = -tVal

  if tVal > 0:
    GPIO.output(tPin, GPIO.HIGH)
  else:
    GPIO.output(tPin, GPIO.LOW)

  
def switch0(value):
   switch_all(0,value)
def switch1(value):
   switch_all(1,value)
def switch2(value):
   switch_all(2,value)
def switch3(value):
   switch_all(3,value)


# ==========
# Subscribe
# ==========
brew_array.subscribe("servo0_cam_pan",servo0);

brew_array.start()


# =======================
#INIT STATE VALUES
# =======================

#Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

servoMin = 50  # Min pulse length out of 4096
servoMax = 500  # Max pulse length out of 4096

#Init switches
for i in range(0,3):
  GPIO.output(arrSwitchPins[i], GPIO.HIGH)


#while (True):
  #PWM.SETPWM(0, 0, SERVO_0)
