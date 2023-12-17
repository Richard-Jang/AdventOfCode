def main():
    input = open('input.txt', 'r').readlines()
    for (index, element) in enumerate(input):
        input[index] = input[index].replace('\n', '')
    seeds = (input[0].split(' '))
    del seeds[0]
    del input[0]
#    x = range(100, 200)
#    for a in x:
#        print(a)
    input.remove('')
    input.append('')
#    print(input.pop(0))
    x = len(separate(input, 'fertilizer-to-water map:', 'water-to-light map:'))
    print(x)

def separate(input, startString, endString):
    numbersArray = []
    while input[0] != startString:
        input.pop(0)
    input.pop(0)
    for count in range(0, input.index(endString) - 1):
        numbersArray.append(input[count])
    print(numbersArray)
    return numbersArray

main()