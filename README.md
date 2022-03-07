# LED UI Demo Using Qt for Python on reTerminal

This is a demo application to control the STA and USR LEDs on the [reTerminal](https://www.seeedstudio.com/ReTerminal-with-CM4-p-4904.html) just by clicking buttons on the LCD.

Here PySide2 is used for the development. PySide2 is the official Python module from the Qt for Python project, which provides access to the complete Qt5 framework. Qt for Python allows you to build interactive user interfaces in a more user friendly way! It is also very flexible to use and has a short learning curve. 

For a step-by-step guide on building your own UI using Qt for Python on the reTerminal, click [here](https://wiki.seeedstudio.com/reTerminal-build-UI-using-Qt-for-Python/)

<p style="text-align:center;"><img src="https://files.seeedstudio.com/wiki/ReTerminal/final-output.png" alt="pir" width="1000" height="auto"></p>

## Install 

First you need to install the necessary libraries. However, if you are using our [compiled Raspberry Pi OS](https://wiki.seeedstudio.com/reTerminal-FAQ/#q2-how-can-i-flash-raspberry-pi-os-which-is-originally-shipped-with-reterminal) or using the Raspberry Pi OS which is shipped with the reTerminal, it already includes these libraries and therefore you can skip this section and move on to the **Usage** section

Access reTerminal using the **onboard LCD, external display or SSH** as explained [here](https://wiki.seeedstudio.com/reTerminal/#log-in-to-raspberry-pi-os-ubuntu-os-or-other-os-using-ssh-over-wi-fi-ethernet) and type the following on a terminal window to install the necessary packages

```sh
sudo apt install python3-pyside2.qtqml python3-pyside2.qtcore python3-pyside2.qtnetwork python3-pyside2.qtgui python3-pyside2.qtwidgets python3-pyside2.qtquick qml-module-qtquick-controls2 qml-module-qtquick-controls
```

## Usage

- **Step 1.** Clone this repo

```sh
git clone https://github.com/lakshanthad/Python_ReTerminalQt5_LED_UI
```

- **Step 2.** Navigate to the **Python_ReTerminalQt5_LED_UI** directory

```sh
cd Python_ReTerminalQt5_LED_UI
```

- **Step 3.** Run the app

```sh
python3 main.py
```

Alternatively, if you want to run the app using the reTerminal LCD, you can double click on the **LED Test** file
