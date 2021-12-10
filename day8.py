with open('inputs/day8.txt') as f:
    lines = [line.rstrip() for line in f]

data = []
for line in lines:
    splitData = line.split(" | ")
    data.append([splitData[0].split(" "), splitData[1].split(" ")])

def part1():
    result = 0
    for item in data:
        right = item[1]
        for digit in right:
            if(len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
                result +=1
    return result

def part2():
    result = 0
    for item in data:
        segmentResult = ""
        meanings = getDigitMeanings(item)
        right = item[1]
        for digit in right:
            segmentResult += str(GetIntForDigit(digit, meanings))
        result += int(segmentResult)
    return result


def GetIntForDigit(digit, meanings):
    for ind in range(0, 10):
        if(len(meanings[ind]) == len(digit) and stringOverlapAmount(meanings[ind], digit) == len(digit)):
            return ind

def getDigitMeanings(signalRange):
    inputSignals = signalRange[0]
    inputSignals.sort(key=len)
    output = {}
    for signal in inputSignals:
       digit = whatDigit(signal, output)
       output[digit] = signal
    return output

def whatDigit(signal, dict):
    # 1
    if(len(signal) == 2):
        return 1
    # 7
    if(len(signal) == 3):
        return 7
    # 4
    if(len(signal) == 4):
        return 4
    # 2, 3, 5
    if(len(signal) == 5):
        if(stringOverlapAmount(dict[1], signal) == 2):
            return 3
        if(stringOverlapAmount(dict[4], signal) == 3):
            return 5
        return 2
    # 0, 6, 9
    if(len(signal) == 6):
        if(stringOverlapAmount(dict[1], signal) == 1):
            return 6
        if(stringOverlapAmount(dict[4], signal) == 4):
            return 9
        return 0
        # 8
    if(len(signal) == 7):
        return 8

def stringOverlapAmount(string1, string2):
    result = 0
    for character in string2:
        if(character in string1):
            result += 1
    return result 
            
        
print(getDigitMeanings(data[0]))
print("part 1: " + str(part1()))
print("part 2: " + str(part2()))
