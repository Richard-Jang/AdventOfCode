def main():
    inputFile = open('input.txt', 'r')
    input = inputFile.readlines()
    winNums = []
    nums = []
    total = []
    sum = 0
    for (index, string) in enumerate(input):
        replaceString = ''
        count = 0
        while string[count] != ':':
            replaceString += string[count]
            count += 1
        newString = input[index].replace(replaceString, '')
        newString = newString.replace(':', '')
        newString = newString.replace('\n', '')
        tempArray = newString.split('|')
        winNums.append(tempArray[0].split(' '))
        winNums = ridSpaces(winNums)
        nums.append(tempArray[1].split(' '))
        nums = ridSpaces(nums)
    for count in range(len(input)):
        if compare(winNums[count], nums[count]) == 0:
            total.append(0)
        else:
            total.append(compare(winNums[count], nums[count]))
    for count in range(len(input)):
        sum += add(count, total)
    print(sum)
    
def compare(array1, array2):
    total = 0
    for val1 in array1:
        for val2 in array2:
            if val1 == val2:
                total += 1
    return int(total)

def add(cardNum, array):
    sum = 1
    if cardNum < len(array):
        for index in range(cardNum + 1, cardNum + array[cardNum] + 1):
            sum += add(index, array)
    return sum

def ridSpaces(array):
    holdArray = []
    for (index, a) in enumerate(array):
        holdArray.append([])
        for value in a:
            if value.isnumeric():
                holdArray[index].append(value)
    return holdArray

main()