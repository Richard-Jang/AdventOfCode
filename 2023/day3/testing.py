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
for a in range(len(symbolMap)):
    b = a + 1
    print(b, symbolMap[a])
for a in range(len(input)):
    print(a)