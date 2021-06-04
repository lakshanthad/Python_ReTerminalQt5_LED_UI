import sys
import os
from PySide2.QtCore import *

class Setting(QObject):

    #staGreen
    @Slot()
    def staGreenOn(self):     
        os.system("sudo sh -c 'echo 255 > /sys/class/leds/usr_led2/brightness'")
    @Slot()
    def staGreenOff(self):     
        os.system("sudo sh -c 'echo 0 > /sys/class/leds/usr_led2/brightness'")

    #staRed
    @Slot()
    def staRedOn(self):     
        os.system("sudo sh -c 'echo 255 > /sys/class/leds/usr_led1/brightness'")
    @Slot()
    def staRedOff(self):     
        os.system("sudo sh -c 'echo 0 > /sys/class/leds/usr_led1/brightness'")

    #usrGreen
    @Slot()
    def usrGreenOn(self):     
        os.system("sudo sh -c 'echo 255 > /sys/class/leds/usr_led0/brightness'")
    @Slot()
    def usrGreenOff(self):     
        os.system("sudo sh -c 'echo 0 > /sys/class/leds/usr_led0/brightness'")

    #close
    @Slot()
    def closeWindow(self):
        sys.exit()