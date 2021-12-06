with open('inputs/day5.txt') as f:
    lines = [line.rstrip() for line in f]

vectors = []
for ind in range(0, len(lines)):
    splitVec = lines[ind].split(" -> ")
    vectors.append([list(map(int, splitVec[0].split(","))),
                   list(map(int, splitVec[1].split(",")))])


    
def fillInLines(useDiagonal):
    ocean = []
    for ind in range(0, 1000):
        hor = [0] * 1000
        ocean.append(hor)
    for vector in vectors:
        x1 = vector[0][0]
        x2 = vector[1][0]
        y1 = vector[0][1]
        y2 = vector[1][1]
        if(x1 == x2):
            for ind in range(min(y1, y2), max(y1, y2) + 1):
                ocean[ind][x1] += 1
        elif(y1 == y2):
            for ind in range(min(x1, x2), max(x1, x2) + 1):
                ocean[y1][ind] += 1
        elif(useDiagonal):
            coord = vector[0].copy()
            ocean[coord[1]][coord[0]] += 1
            if(y1 > y2 and x1 > x2):
                while(coord != vector[1]):
                    coord[0] -= 1
                    coord[1] -= 1
                    ocean[coord[1]][coord[0]] += 1
            elif(y1 > y2 and x1 < x2):
                while(coord != vector[1]):
                    coord[0] += 1
                    coord[1] -= 1
                    ocean[coord[1]][coord[0]] += 1
            elif(x1 > x2):
                while(coord != vector[1]):
                    coord[0] -= 1
                    coord[1] += 1
                    ocean[coord[1]][coord[0]] += 1
            else:
                while(coord != vector[1]):
                    coord[0] += 1
                    coord[1] += 1
                    ocean[coord[1]][coord[0]] += 1
    return ocean

def getLineOverlaps(grid):
    summation = 0
    for y in range (len(grid)):
        for x in range (len(grid[0])):
            if(grid[y][x] >= 2):
                summation += 1
    return summation
                

print("part 1: " + str(getLineOverlaps(fillInLines(False))))
print("part 2: " + str(getLineOverlaps(fillInLines(True))))
