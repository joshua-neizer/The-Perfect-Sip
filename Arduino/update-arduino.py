import json
import re

def updateLine(name, value):
    if 'RGB' in name:
        return 'int ' + name + '[] = {' + hex_to_rgb(value) + '};\n'
    else:
        return 'int ' + name + ' = ' + str(value) + ';\n'

def hex_to_rgb(hex):
    rgb = tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    return str(rgb)

jsonFile = './preferences.json'
ArduinoFile = './tps/tps.ino'



with open(jsonFile) as f:
  preference = json.load(f)

# with is like your try .. finally block in this case
with open(ArduinoFile, 'r') as file:
    # read a list of lines into data
    data = file.readlines()

i = 9
keys = list(preference.keys())
for key in keys:
    data [i] = updateLine(key, preference[key])
    i += 1


# and write everything back
with open(ArduinoFile, 'w') as file:
    file.writelines( data )