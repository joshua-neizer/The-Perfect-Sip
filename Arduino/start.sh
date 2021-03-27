#!/bin/bash

# https://rootsaid.com/arduino-cli/
# https://create.arduino.cc/projecthub/jithinsanal1610/arduino-cli-c26e6e

# Updates the arduino code
python3 update-arduino.py

# Compiles and verifies code
sudo arduino-cli compile --fqbn arduino:avr:uno --libraries="/usr/share/arduino/libraries" IR_TempTest/

# Uploads and runs code to the arduino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno IR_TempTest/