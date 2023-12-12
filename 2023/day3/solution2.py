def main():
    inputFile = open('input.txt', 'r')
    input = inputFile.readlines()
    symbols = ['*']
    symbolMap = []
    sum = 0
    for (index, lines) in enumerate(input):
        symbolMap.append([])                                                                                 # create 2d array that maps index of symbols
        for (charIndex, char) in enumerate(lines):
            for symbol in symbols:
                if char == symbol:
                    symbolMap[index].append(charIndex)
    for lineNum in range(len(input)):
        if len(symbolMap[lineNum]) == 0:
            continue
        for symbolIndex in symbolMap[lineNum]:
            if lineNum == 0:
                sum += checkAdjacent(symbolIndex, '', input[lineNum], input[lineNum + 1])
            elif lineNum == (len(input) - 1):
                sum += checkAdjacent(symbolIndex, input[lineNum - 1], input[lineNum], '')
            else:
                sum += checkAdjacent(symbolIndex, input[lineNum - 1], input[lineNum], input[lineNum + 1])
    print(sum)

def checkAdjacent(symbolIndex, upperString, string, lowerString):
    numbers = []
    strings = []
    if upperString != '':
        strings.append(upperString)
    if string != '':
        strings.append(string)
    if lowerString != '':
        strings.append(lowerString)
    for strn in strings:
        if strn != '':
            if checkMiddle(symbolIndex, strn) != '':
                numbers.append(checkMiddle(symbolIndex, strn))
                continue
            if checkBack(symbolIndex, strn) != '':
                numbers.append(checkBack(symbolIndex, strn))
            if checkFront(symbolIndex, strn) != '':
                numbers.append(checkFront(symbolIndex, strn))
    if len(numbers) == 2:
        return int(numbers[0]) * int(numbers[1])
    else:
        return 0

def checkMiddle(index, string):
    finalString = ''
    if string[index].isnumeric():
        finalString = checkFront(index, string) + string[index] + checkBack(index, string)
    return finalString

def checkFront(index, string):
    currentNum = index - 1
    finalString = ''
    while (currentNum >= 0) and string[currentNum].isnumeric():
        finalString = string[currentNum] + finalString
        currentNum -= 1
    return finalString

def checkBack(index, string):
    currentNum = index + 1
    finalString = ''
    while (currentNum <= len(string) - 1) and string[currentNum].isnumeric():
        finalString += string[currentNum]
        currentNum += 1
    return finalString

main()