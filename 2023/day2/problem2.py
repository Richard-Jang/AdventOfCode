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
    verifyInstance = [0, 0, 0]
    for result in gameResults:
        subResult = result.split(' ')
        for (index, element) in enumerate(subResult):
            for (colorIndex, color) in enumerate(verify):
                if element.replace(',', '') == color:
                    if verifyInstance[colorIndex] < int(subResult[index - 1]):
                        verifyInstance[colorIndex] = int(subResult[index - 1])
    print(verifyInstance, gameNumStr)
    sum += (verifyInstance[0] * verifyInstance[1] * verifyInstance[2])
print(sum)