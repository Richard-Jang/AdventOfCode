def main():
    inputFile = open('input.txt', 'r')
    input = inputFile.readlines()
    winNums = []
    nums = []
    for (index, string) in enumerate(input):
        replaceString = 'Card ' + str(index + 1) + ': '
        newString = input[index].replace(replaceString, '')
        print(newString)
main()
def pointValue(times):
    value = 1
    for _ in range(times - 1):
        value += value
    return value