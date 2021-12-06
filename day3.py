with open('inputs/day3.txt') as f:
    lines = [line.rstrip() for line in f]

bitLength = len(lines[0])
def getMostCommonBits(lines):
    zeroBits = [0] * bitLength
    oneBits = [0] * bitLength
    for ind in range(0, len(lines)):
        for charInd in range(0, len(lines[ind])):
            if(lines[ind][charInd] == '1'):
                oneBits[charInd] += 1
            else:
                zeroBits[charInd] += 1
    return (zeroBits, oneBits)

result = getMostCommonBits(lines)
gamma = ""
epsilon = ""
for ind in range(0, bitLength):
    if(result[0][ind] > result[1][ind]):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print("part 1: " + str(int(gamma, 2) * int(epsilon, 2)))


def moreLeastBitTuple(zeroBits, oneBits, ind):
    return ('0', '1') if zeroBits[ind] > oneBits[ind] else ('1', '0')

oxygen = lines.copy()
for ind in range(0, bitLength):
    if(len(oxygen) == 1):
        break
    mostCommon = getMostCommonBits(oxygen)
    moreLeast = moreLeastBitTuple(mostCommon[0], mostCommon[1], ind)
    oxygen = list(filter(lambda x: (x[ind] == moreLeast[0]), oxygen))

carbondioxide = lines.copy()
for ind in range(0, bitLength):
    if(len(carbondioxide) == 1):
        break
    mostCommon = getMostCommonBits(carbondioxide)
    moreLeast = moreLeastBitTuple(mostCommon[0], mostCommon[1], ind)
    carbondioxide = list(
        filter(lambda x: (x[ind] == moreLeast[1]), carbondioxide))

print("part 2: " + str(int(oxygen[0], 2) * int(carbondioxide[0], 2)))
