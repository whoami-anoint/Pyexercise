myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Anoint": "Abhishek",
    "Marks": {1,2,5},
    "anotherdict": {'Hackerone': 'Platform'},
    1 : 2 
}

# Dictionary Methods
print(list(myDict.keys()))  # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Sudeepa": "Friend",
    "Sareeta": "Friend",
    "Priyanka": "Friend",
    "Harry": "A dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Harry")) # Prints value associated with key "Harry"
print(myDict["Harry"]) # Prints value associated with key "Harry"

# The difference between .get and [] syntax in dictionary
print(myDict.get("Harry2")) # returns none as Harry is not present in the dictionary
# print(myDict["Harry2"]) # throws an error as Harry2 is not present in the dictionary

