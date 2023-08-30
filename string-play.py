store = []
str = 'Contact: DionicioEmail: diongartist@yahoo.comPhone: 1.956.778.5854Address: 1221 W Campbell RdCity: Richardson'
ind = str.find("Email")
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
print(str)