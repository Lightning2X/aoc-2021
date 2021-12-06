with open('inputs/day4.txt') as f:
    lines = [line.rstrip() for line in f]
    
bingoNumbers = map(int, lines[0].split(","))
cards = []
currentCard = []
for ind in range(2, len(lines)):
    if(lines[ind] == ""):
        cards.append(currentCard)
        currentCard = []
        continue
    currentCard.append(list(map(lambda x: (int(x), False), lines[ind].split())))

def cardHasWon(card):
    length = len(card)
    row = 0
    cols = [0] * length
    for y in range(0, length):
        row = 0;
        for x in range(0, length):
            if(card[y][x][1]):
                row += 1;
                cols[x] += 1;
        if(row == length or len(list(filter(lambda x: (x == length), cols))) > 0):
            return True
    return False
    
            
def markCard(card, num):
    length = len(card)
    for y in range(0, length):
        for x in range(0, length):
            if(card[y][x][0] == num):
                card[y][x] = (card[y][x][0], True)

def getSumUnmarked(card): 
    length = len(card)
    summation = 0
    for y in range(0, length):
        for x in range(0, length):
            if(not card[y][x][1]):
                summation += card[y][x][0]
    return summation

def part1():
    cardsCopy = cards.copy()
    for number in bingoNumbers:
        for card in cardsCopy:
            markCard(card, number)
            if(cardHasWon(card)): 
                return getSumUnmarked(card) * number


print("part 1: " + str(part1()))

def part2():
    cardsCopy = cards.copy()
    lastToWin = []
    lastNum = 0
    for number in bingoNumbers:
        for ind in reversed(range(0, len(cardsCopy))):
            card = cardsCopy[ind]
            markCard(card, number)
            if(cardHasWon(card)): 
                lastToWin = card
                lastNum = number
                cardsCopy.remove(card)
    return getSumUnmarked(lastToWin) * lastNum
    

print("part 2: " + str(part2()))

