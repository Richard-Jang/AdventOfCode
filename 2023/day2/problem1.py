inputFile = open('input.txt', 'r')
input = inputFile.readlines()
sum = 0
verify = ['red', 'green', 'blue']
verifyTotal = [12, 13, 14]
for game in input:
    isAllowed = True
    gameString = game.replace('Game ', '')
    gameString = gameString.replace('\n', '')
    gameNumStr = ''
    for index in range(0, 3):
        if gameString[index].isnumeric():
            gameNumStr += gameString[index]
    while gameString[0] != ' ':
        gameString = gameString[1 : : ]
    gameResults = gameString.split(';')
    for result in gameResults:
        verifyInstance = [0, 0, 0]
        subResult = result.split(' ')
        for (index, element) in enumerate(subResult):
            for (colorIndex, color) in enumerate(verify):
                if element.replace(',', '') == color:
                    verifyInstance[colorIndex] += int(subResult[index - 1])
        for (index, amount) in enumerate(verifyTotal):
            if amount < verifyInstance[index]:
                isAllowed = False
    if isAllowed:
        sum += int(gameNumStr)
print(sum)