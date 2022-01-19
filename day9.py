with open('inputs/day9.txt') as f:
    lines = [line.rstrip() for line in f]

grid = []
for line in lines:
    grid.append(list(map(int, line)))

height = len(grid)
width = len(grid[0])

def getLowPoints(grid):
    lowPoints = []
    for y in range(0, height):
        for x in range(0, width):
            currentPos = grid[y][x]
            if((x <= 0 or grid[y][x - 1] > currentPos)
               and (x >= width - 1 or grid[y][x + 1] > currentPos)
               and (y >= height - 1 or grid[y + 1][x] > currentPos)
               and (y <= 0 or grid[y - 1][x] > currentPos)):
                lowPoints.append((y, x))
    return lowPoints


def outOfbounds(y, x):
    return x < 0 or x >= width or y >= height or y < 0

def getBasinSize(grid, lowPoint):
    # This int is wrapped in a list so it becomes mutable and is passed by reference
    accum = [0]
    visited = []
    surroundingPoints(grid, lowPoint, visited, accum)
    return accum[0]
  
def surroundingPoints(grid, point, visited, accum):
    y = point[0]
    x = point[1]
    if(outOfbounds(y, x)):
        return
    if(point in visited):
        return 
    if(grid[y][x] == 9):
        return
    
    accum[0] += 1
    visited.append(point)
    surroundingPoints(grid, (y, x + 1), visited, accum)
    surroundingPoints(grid, (y, x - 1), visited, accum)
    surroundingPoints(grid, (y + 1, x), visited, accum)
    surroundingPoints(grid, (y - 1, x), visited, accum)
     

lowPoints = getLowPoints(grid)
print("part 1: " + str(sum(map(lambda t: grid[t[0]][t[1]] + 1, lowPoints))))
basins = list(map(lambda t: getBasinSize(grid, t), lowPoints))
basins.sort(reverse=True)
print("part 2: " + str(basins[0] * basins[1] * basins[2]))
