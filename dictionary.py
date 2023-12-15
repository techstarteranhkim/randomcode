dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

def addItem(key, value):
    dictionary[key] = value

def printValue(key):
    print(dictionary[key])

def valueIsEqual(key,value):
    return dictionary[key]==value

def deleteItem(key):
    del dictionary[key]

def printKeys():
    for item in dictionary:
        print(item)

def printValues():
    for item in dictionary:
        print(dictionary[item])

addItem("Horst", "Kurt")
#testing code
print(dictionary["Horst"])
addItem("one","1")
addItem("two", "2")
printValue("one")
printValue("two")
print(valueIsEqual("one","1"))
print(valueIsEqual("two","1"))
deleteItem("one")
printKeys()
printValues()