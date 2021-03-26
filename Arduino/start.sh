#!/bin/bash

alias 'arduino-cli'='~/go/src/github.com/arduino/arduino-cli/bin/arduino-cli'

# Updates the arduino code
python3 update-arduino.py

# Compiles and verifies code
arduino-cli compile --fqbn arduino:avr:uno run/

# Uploads and runs code to the arduino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno run/