inputFile = open('input.txt', 'r')
input = inputFile.readlines()
sum = 0
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for string in input:
    numList = [[]*2]                                                    # index, value
    for index, value in enumerate(string):                              # numList
        if value.isnumeric():
            numList.append([index, int(value)])
    val = 0
    for num in digits:                                                  # letterIndex
        stringCopy = string
        while stringCopy.find(num) != -1:
            numList.append([stringCopy.find(num), val])
            stringCopy = stringCopy.replace(num, '_'*len(num), 1)
        val += 1
    numList.sort()
    numList.remove([])
    #print(numList, (numList[0][1] * 10 + numList[-1][1]))
    sum += (numList[0][1] * 10 + numList[-1][1])
print(sum)