with open('inputs/day7.txt') as f:
    lines = [line.rstrip() for line in f]

crabs = list(map(int, lines[0].split(",")))
minimum = min(crabs)
maximum = max(crabs)
costspart1 = [0] * (maximum - minimum)
costspart2 = [0] * (maximum - minimum)

def calculateCosts(crabs, ind):
    cost1 = 0
    cost2 = 0
    for crab in crabs:
        n = abs(crab - ind)
        cost1 += n
        cost2 += int((n * (1 + n)) / 2)
    return (cost1, cost2)


for ind in range(minimum, maximum):
    costs = calculateCosts(crabs, ind)
    costspart1[ind] = costs[0]
    costspart2[ind] = costs[1]

print(min(costspart1))
print(min(costspart2))
