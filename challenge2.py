## CCC Challenge 2 ##

def getHeavyLetter(array):
    if (len(array) >= 2) and (len(set(array)) == 1): # Needs at least 2 values to be considered repeating | Check if there is only one unique value (repeating) 
        return array[0]
    return None

def getInput():
    userInput = input()
    listOfArgs = userInput.split()
    try: 
        return int(listOfArgs[0]), int(listOfArgs[1]) # Amount of lines [T] | Expected length of each line [N] (unused)
    except:
        raise ValueError("Numbers must be integers")

def hasRepeatWithoutIntersection(array, disjointArray):
    heavyLetter = getHeavyLetter(array)
    if heavyLetter and (not heavyLetter in disjointArray):
        return True
    return False

def process(line):
    # Parse Inputs
    array1 = line[::2]
    array2 = line[1::2]

    if (hasRepeatWithoutIntersection(array1, array2) ^ hasRepeatWithoutIntersection(array2, array1)): # XOR distinction, both cannot be alternating heavies
        return "T"  # True
    return "F"      # False

output = "" # Charbuilder
t,n = getInput()
for _ in range(t):
    output += process(input()) + '\n'
print(output.removesuffix('\n')) 