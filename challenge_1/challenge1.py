def getN():
    try:
        maxNumbers = input()
        return int(maxNumbers)
    except:
        raise ValueError(f"Recieved {type(maxNumbers)} => Expected type Integer")

def ensureEven(number):
    if number % 2 == 0:
        return number
    raise ValueError("'N' must be an even integer")

def getInput():
    arrayOfInput = []
    maxNumbers = ensureEven(getN())
    for _ in range(maxNumbers):
        arrayOfInput.append(input())
    return maxNumbers, arrayOfInput

def process(radius, halfTheList, originalList):
    totalWatchers = 0
    for index, value in enumerate(halfTheList):
        if value == originalList[index+radius]:
            totalWatchers += 2
    return totalWatchers

N,H = getInput()
radius = N // 2
halfTheList = H[:radius]
print(process(radius, halfTheList, H))