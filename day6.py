with open('inputs/day6.txt') as f:
    lines = [line.rstrip() for line in f]

fishes = list(map(int, lines[0].split(",")))

def fastSimulation(cycles):
    sim = [0] * 9
    for ind in fishes:
        sim[ind] += 1
    for ind in range(cycles):
        day = ind % len(sim)
        sim[(day + 7) % len(sim)] += sim[day]
    return sum(sim)

print("part 1: " + str(fastSimulation(80)))
print("part 2: " + str(fastSimulation(256)))
