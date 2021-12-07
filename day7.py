with open('inputs/day7.txt') as f:
    lines = [line.rstrip() for line in f]

crabs = list(map(int, lines[0].split(",")))
minimum = min(crabs)
maximum = max(crabs)
costspart1 = [0] * (maximum - minimum)
costspart2 = [0] * (maximum - minimum)

def calculateCostpart1(crabs, ind):
    cost = 0
    for crab in crabs:
        cost += abs(crab - ind)
    return cost


def calculateCostpart2(crabs, ind):
    cost = 0
    for crab in crabs:
        num = 0
        # calculate triangular number
        for sumNum in range(1, abs(crab - ind) + 1):
            num += sumNum
        cost += num
    return cost

for ind in range(minimum, maximum):
    costspart1[ind] = calculateCostpart1(crabs, ind)
    costspart2[ind] = calculateCostpart2(crabs, ind)

print(min(costspart1))
print(min(costspart2))
