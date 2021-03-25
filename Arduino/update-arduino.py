import json

jsonFile = './preferences.json'
ArduinoFile = './run/run.ino'

with open(jsonFile) as f:
  preference = json.load(f)

# with is like your try .. finally block in this case
with open(ArduinoFile, 'r') as file:
    # read a list of lines into data
    data = file.readlines()

i = 3
keys = list(preference.keys())
for key in keys:
    data [i] = "const char* " + key + " = " + preference [key] + ";\n"
    i += 1
# and write everything back
with open(ArduinoFilea, 'w') as file:
    file.writelines( data )