import json

def updateLine(name, value):
    try:
        int(value)
        return 'const int ' + name + ' = ' + str(value) + ';\n'
    except:
        return 'const String ' + name + ' = "' + value + '";\n'

jsonFile = './preferences.json'
ArduinoFile = './run/run.ino'



with open(jsonFile) as f:
  preference = json.load(f)

# with is like your try .. finally block in this case
with open(ArduinoFile, 'r') as file:
    # read a list of lines into data
    data = file.readlines()

i = 0
keys = list(preference.keys())
for key in keys:
    data [i] = updateLine(key, preference[key])
    i += 1


# and write everything back
with open(ArduinoFile, 'w') as file:
    file.writelines( data )