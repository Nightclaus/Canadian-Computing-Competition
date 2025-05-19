arrayOfInput = []
maxNumbers = int(input())
for _ in range(maxNumbers):
    arrayOfInput.append(input())

radius = maxNumbers // 2
halfTheList = arrayOfInput[:radius]

total = 0
for index, value in enumerate(halfTheList):
    if value == arrayOfInput[index+radius]:
        total += 2

print(total)