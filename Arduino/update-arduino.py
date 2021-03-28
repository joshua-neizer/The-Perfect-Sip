import json
import re

def updateLine(name, value):
    if 'RGB' in name:
        return 'int ' + name + '[] = {' + str(re.findall("[0-9]+, [0-9]+, [0-9]+", value)[0]) + '};\n'
    else:
        return 'int ' + name + ' = ' + str(value) + ';\n'

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