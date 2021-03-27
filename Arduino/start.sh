#!/bin/bash

# https://rootsaid.com/arduino-cli/
# https://create.arduino.cc/projecthub/jithinsanal1610/arduino-cli-c26e6e

# Updates the arduino code
python3 update-arduino.py

ps -ef | grep "python3 getSerial.py" | awk '{print $2}' | xargs sudo kill

# Compiles and verifies code
sudo arduino-cli compile --fqbn arduino:avr:uno --libraries="/usr/share/arduino/libraries" IR_TempTest/

# Uploads and runs code to the arduino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno IR_TempTest/

python3 getSerial.py &