inputFile = open('input.txt', 'r')
input = inputFile.readlines()
sum = 0
for string in input:
    numList = []
    for char in string:
        if char.isnumeric():
            numList.append(int(char))
    sum += (numList[0] * 10 + numList[-1])
print(sum)