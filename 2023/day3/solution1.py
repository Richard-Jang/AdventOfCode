def main():
    inputFile = open('input.txt', 'r')
    input = inputFile.readlines()
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '+', '=', '-']
    symbolMap = []
    sum = 0
    for (index, lines) in enumerate(input):
        symbolMap.append([])                                                                                 # create 2d array that maps index of symbols
        for (charIndex, char) in enumerate(lines):
            for symbol in symbols:
                if char == symbol:
                    symbolMap[index].append(charIndex)
    for lineNum in range(len(input)):
        if lineNum == 0:
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum]) or 0)
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum + 1]) or 0)
        elif lineNum == (len(input) - 1):
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum - 1]) or 0)
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum]) or 0)
        else:
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum - 1]) or 0)
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum]) or 0)
            sum += int(checkAdjacent2D(symbolMap[lineNum], input[lineNum + 1]) or 0)
    print(sum)

def checkAdjacent2D(symbolArray, string):                                                                  # left and right; check for numbers in adjacent tiles on one line, symbolArray (mapping index of location), string (line to search)
    sum = 0
    for num in symbolArray:
        if string[num].isnumeric():                                                                      # if +0 has number
            print(checkFront(num, string) + string[num] + checkBack(num, string), 'middle')
            sum += int(checkFront(num, string) + string[num] + checkBack(num, string))
        else:
            if (num > 0) and (string[num - 1].isnumeric()):                                                  # if -1 has number
                print(checkFront(num, string), 'front')
                sum += int(checkFront(num, string))
            if (num < (len(string) - 1)) and string[num + 1].isnumeric():                                    # if +1 has number
                print(checkBack(num, string), 'back')
                sum += int(checkBack(num, string))
    return sum

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