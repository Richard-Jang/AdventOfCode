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
    print(symbolMap)
    for lineNum in range(len(input)):
        if len(symbolMap[lineNum]) == 0:
            print('contd')
            continue
        for symbolIndex in symbolMap[lineNum]:
            print(lineNum)
            if lineNum == 0:
                sum += checkAdjacent(symbolIndex, '', input[lineNum], input[lineNum + 1])
            elif lineNum == (len(input) - 1):
                sum += checkAdjacent(symbolIndex, input[lineNum - 1], input[lineNum], '')
            else:
                sum += checkAdjacent(symbolIndex, input[lineNum - 1], input[lineNum], input[lineNum + 1])
    print(sum)

def checkAdjacent(symbolIndex, upperString, string, lowerString):
    numbers = strings = []
    if upperString != '':
        strings.append(upperString)
    if string != '':
        strings.append(string)
    if lowerString != '':
        strings.append(lowerString)
    for str in strings:
        if checkMiddle(symbolIndex, string) != '':
            numbers.append(checkMiddle(symbolIndex, str))
        if checkBack(symbolIndex, string) != '':
            numbers.append(checkBack(symbolIndex, str))
        if checkFront(symbolIndex, string) != '':
            numbers.append(checkFront(symbolIndex, str))
    if len(numbers) == 2:
        print(numbers)
        return numbers[0] * numbers[1]
    else:
        return 0

def checkMiddle(index, string):
    finalString = ''
    if string[index].isnumeric():
        finalString = checkFront(index, string) + string[index] + checkBack(index, string)
        #print('middle')
    return finalString

def checkFront(index, string):
    currentNum = index - 1
    finalString = ''
    while (currentNum >= 0) and string[currentNum].isnumeric():
        finalString = string[currentNum] + finalString
        currentNum -= 1
    #print('front')
    return finalString

def checkBack(index, string):
    currentNum = index + 1
    finalString = ''
    while (currentNum <= len(string) - 1) and string[currentNum].isnumeric():
        finalString += string[currentNum]
        currentNum += 1
    #print('back')
    return finalString

main()