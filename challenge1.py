def getInput():
    arrayOfInput = []
    maxNumbers = int(input())
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