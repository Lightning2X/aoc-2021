with open('inputs/day6.txt') as f:
    lines = [line.rstrip() for line in f]

fishes = list(map(int, lines[0].split(",")))

def simulationStep(fish):
    for ind in reversed(range(0, len(fish))):
        if(fish[ind] == 0):
            fish.append(8)
            fish[ind] = 6
            continue
        fish[ind] -= 1
    return fish

def simulation(cycles):
    fishies = fishes.copy()
    for num in range(0, cycles):
        fishies = simulationStep(fishies)
    return len(fishies)


print("part 1: " + str(simulation(80)))

def fastSimulation(cycles):
    sim = [0] * 9
    for ind in fishes:
        sim[ind] += 1
    for ind in range(cycles):
        day = ind % len(sim)
        sim[(day + 7) % len(sim)] += sim[day]
    return sum(sim)


print("part 2: " + str(fastSimulation(256)))
