# mutable : Values can be changed.
# Unordered
# Indexed
# Cannot contain duplicate keys


myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Anoint": "Abhishek",
    "Marks": {1,2,5},
    "anotherdict": {'Hackerone': 'Platform'}
}
# print(myDict['Anoint'])
# print(myDict['Harry'])
myDict["Marks"] = {45,72,38}
print(myDict["Marks"])
print(myDict["anotherdict"]["Hackerone"])


