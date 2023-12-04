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
            sum += int(checkAdjacent(symbolMap[lineNum], input[lineNum]) or 0)
            sum += int(checkAdjacent(symbolMap[lineNum + 1], input[lineNum + 1]) or 0)
        elif lineNum == (len(input) - 1):
            sum += int(checkAdjacent(symbolMap[lineNum], input[lineNum]) or 0)
            sum += int(checkAdjacent(symbolMap[lineNum - 1], input[lineNum - 1]) or 0)
        else:
            sum += int(checkAdjacent(symbolMap[lineNum], input[lineNum]) or 0)
            sum += int(checkAdjacent(symbolMap[lineNum - 1], input[lineNum - 1]) or 0)
            sum += int(checkAdjacent(symbolMap[lineNum + 1], input[lineNum + 1]) or 0)
    print(sum)

def checkAdjacent(symbolArray, string):                                                                  # check for numbers in adjacent tiles on one line
    for num in symbolArray:
        if (num > 0) and (string[num - 1].isnumeric()):                                                  # if -1 has number
            return checkFront(num, string)
        if string[num].isnumeric():                                                                      # if +0 has number
            return checkFront(num, string) + string[num] + checkBack(num, string)
        if (num < (len(string) - 1)) and string[num + 1].isnumeric():                                    # if +1 has number
            print(checkBack(num, string))
            return checkBack(num, string)

def checkFront(index, string):
    currentNum = index - 1
    finalString = ''
    while (currentNum >= 0) and string[currentNum].isnumeric():
        finalString = string[currentNum] + finalString
        currentNum += 1
    return finalString

def checkBack(index, string):
    currentNum = index + 1
    finalString = ''
    while (currentNum <= len(string) - 1) and string[currentNum].isnumeric():
        finalString += string[currentNum]
        currentNum += 1
    return finalString

main()