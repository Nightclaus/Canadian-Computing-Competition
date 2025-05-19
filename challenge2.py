## CCC Challenge 2 ##

def isSame(array):
    if len(array) < 2:
        return False, None ## Too small
    if len(set(array)) == 1:
        return True, array[0]
    return False, None

def getInput():
    userInput = input()
    listOfArgs = userInput.split()
    try: 
        amountOL= int(listOfArgs[0])
        lengthOL = int(listOfArgs[1]) # Unused bc we using set
    except:
        raise ValueError("Numbers must be integers")

    # OL := ___ of Lines
    return amountOL, lengthOL

def challenge2(amountOL, lengthOL):
    output = ""
    for _ in range(amountOL):
        line = input()
        #print(line[::2])
        array1 = line[::2]
        array2 = line[1::2]

        bool1, value1 = isSame(array1)
        bool2, value2 = isSame(array2)
        if bool1:
            if not value1 in array2: ## Check if consecuatuve
                output+="T\n" # True
                continue
        elif bool2:
            if not value2 in array1: ## Check if consecuatuve
                output+="T\n" # True
                continue
        output+="F\n" # False

    print(output.removesuffix("\n")) # Avoid having to iterate if it was an array instead

a,b = getInput()
challenge2(a,b)