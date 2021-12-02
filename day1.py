with open('inputs/day1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

result1 = 0
for ind in range(0, len(lines)):
    if(ind == 0):
        continue
    if(lines[ind] > lines[ind -1]):
        result1 += 1

print("part 1: " + str(result1))

result2 = 0
for ind in range(0, len(lines)):
    if(ind < 2):
        continue
    if(ind + 1 == len(lines)):
        continue
    
    if(lines[ind + 1] > lines[ind - 2]):
        result2 += 1
print("part 2: " + str(result2))
