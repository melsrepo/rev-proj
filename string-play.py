store = []
str = 'Contact: DionicioEmail: diongartist@yahoo.comPhone: 1.956.778.5854Address: 1221 W Campbell RdCity: Richardson'
str = str.replace('Email', ',Email').replace('Phone', ',Phone').replace('Address', ',Address').replace('City', ',City')
output = str.split(',')
print("our first split:")
print(output)
print("-----------------------")
print("our second...etc split")
dict = {}
for info in output:
    info = info.split(':')
    print(info)
    dict[info[0].strip()] = info[1].strip()
print("-----------------------")
print("our nice dict")

for key in dict:
    print(key + "--" + dict[key])

'''ind = str.find("Email")
section = str[:ind]
print(section)
str = str.replace(section, "")
print(str)

ind = str.find("Phone")
section = str[:ind]
print(section)
str = str.replace(section, "")
print(str)

ind = str.find("Address")
section = str[:ind]
print(section)
str = str.replace(section, "")
print(str)

ind = str.find("City")
section = str[:ind]
print(section)
str = str.replace(section, "")
print(str)'''