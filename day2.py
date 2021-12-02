with open('inputs/day2.txt') as f:
    lines = [line.rstrip() for line in f]

depth1 = 0
horizontal1 = 0
for ind in range(0, len(lines)):
    split = lines[ind].split(" ")
    amount = int(split[1])
    if(split[0] == "down"):
        depth1 += amount
    if(split[0] == "up"):
        depth1 -= amount
    if(split[0] == "forward"):
        horizontal1 += amount

print("part 1: " + str(horizontal1 * depth1))

depth2 = 0
horizontal2 = 0
aim = 0
for ind in range(0, len(lines)):
    split = lines[ind].split(" ")
    amount = int(split[1])
    if(split[0] == "down"):
        aim += amount
    if(split[0] == "up"):
        aim -= amount
    if(split[0] == "forward"):
        horizontal2 += amount
        depth2 += (aim * amount)

print("part 2: " + str(horizontal2 * depth2))
