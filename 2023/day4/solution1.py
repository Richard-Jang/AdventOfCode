def main():
    inputFile = open('input.txt', 'r')
    input = inputFile.readlines()
    winNums = []
    nums = []
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
        #print(count)
        if compare(winNums[count], nums[count]) == 0:
            continue
        else:
            #print(compare(winNums[count], nums[count]) or 0)
            sum += pointValue(compare(winNums[count], nums[count]) or 0)
    print(sum)
    
    
def compare(array1, array2):
    total = 0
    for val1 in array1:
        for val2 in array2:
            if val1 == val2:
                total += 1
    return int(total)

def pointValue(times):
    times = int(str(times))
    value = 1
    for _ in range(times - 1):
        value += value
    return value

def compare(winVal, myVal):
    total = 0

def ridSpaces(array):
    holdArray = []
    for (index, a) in enumerate(array):
        holdArray.append([])
        for value in a:
            if value.isnumeric():
                holdArray[index].append(value)
    return holdArray

main()