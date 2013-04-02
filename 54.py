#!/usr/bin/python

def rank(x):
    if x == 'A':
        return 14
    elif x == 'K':
        return 13
    elif x == 'Q':
        return 12
    elif x == 'J':
        return 11
    elif x == 'T':
        return 10
    else:
        return ord(x) - ord('0')

def isStrait(hand):
    for i in xrange(4):
        if hand[i][0] + 1 != hand[i+1][0]:
            return False
    return True

def isFlush(hand):
    for i in xrange(4):
        if hand[i][1] != hand[i+1][1]:
            return False
    return True

def isFour(hand):
    x = hand[2][0]
    if hand[0][0] == x:
        for i in xrange(4):
            if hand[i][0] != x:
                return (False,0,0)
        return (True,x,hand[-1][0])
    else:
        for i in xrange(4):
            if hand[-i][0] != x:
                return (False,0,0)
        return (True,x,hand[0][0])

def isThree(hand):
    x = hand[2][0]
    cnt = 0
    other = []
    for h in hand:
        if h[0] == x:
            cnt += 1
        else:
            other.append(h[0])
    if cnt == 3:
        return (True, x, max(other), min(other))
    else:
        return (False,0,0,0)

def isTwoPair(hand):
    cnt = {}
    for h in hand:
        cnt[h[0]] = 0
    for h in hand:
        cnt[h[0]] += 1
    pairs = []
    other = []
    for i in cnt:
        if cnt[i] == 2:
            pairs.append(i)
        else:
            other.append(i)
    if len(pairs) == 2:
        return (True,max(pairs),min(pairs),other[0])
    else:
        return (False,0,0,0)

def isOnePair(hand):
    cnt = {}
    for h in hand:
        cnt[h[0]] = 0
    for h in hand:
        cnt[h[0]] += 1
    pairs = []
    other = []
    for i in cnt:
        if cnt[i] == 2:
            pairs.append(i)
        else:
            other.append(i)
    if len(pairs) == 1:
        other.sort()
        return (True,pairs[0],other[-1],other[-2],other[-3])
    else:
        return (False,0,0,0,0)

def isFullHouse(hand):
    x = hand[0][0]
    y = hand[-1][0]
    x_cnt = 0
    y_cnt = 0
    for i in xrange(5):
        if hand[i][0] == x:
            x_cnt += 1
        elif hand[i][0] == y:
            y_cnt += 1
        else:
            return (False,0,0)
    if x_cnt > y_cnt:
        return (True,x,y)
    else:
        return (True,y,x)

def scoreHighcard(hand):
    score = hand[-1][0]
    score *= 20
    score += hand[-2][0]
    score *= 20
    score += hand[-3][0]
    score *= 20
    score += hand[-4][0]
    score *= 20
    score += hand[-5][0]
    return score


# assign score to a poker hand
# takes a string e.g. "3D 6D 7H QD QS"
def score(hand):
    # break into pairs of (rank,suit)
    hand = map(lambda x: (rank(x[0]), x[1]),hand.split())
    hand.sort()
    if isStrait(hand) and isFlush(hand):
        # 10 mil + high card
        return 12000000 + hand[-1][0]
    x = isFour(hand)
    if x[0]:
        return 11000000 + 1000 * x[1] + x[2]
    x = isFullHouse(hand)
    if x[0]:
        return 10000000 + 1000 * x[1] + x[2]
    if isFlush(hand):
        return 7000000 + scoreHighcard(hand)
    if isStrait(hand):
        return 6000000 + hand[-1][0]
    x = isThree(hand)
    if x[0]:
        return 5000000 + 10000 * x[1] + 100 * x[2] + x[3]
    x = isTwoPair(hand)
    if x[0]:
        return 4000000 + 10000 * x[1] + 100 * x[2] + x[3]
    x = isOnePair(hand)
    if x[0]:
        score = x[1]
        score *= 20
        score += x[2]
        score *= 20
        score += x[3]
        score *= 20
        score += x[4]
        return 3000000 + score
    return scoreHighcard(hand)

hand1 = "5H 5C 6S 7S KD"
hand2 = "2C 3S 8S 8D TD"

hand1 = "5D 8C 9S JS AC"
hand2 = "2C 5C 7D 8S QH"

hand1 = "2D 9C AS AH AC"
hand2 = "3D 6D 7D TD QD"

hand1 = "4D 6S 9H QH QC"
hand2 = "3D 6D 7H QD QS"

hand1 = "2H 2D 4C 4D 4S"
hand2 = "3C 3D 3S 9S 9D"

player1 = 0
f = open('poker.txt','r')
for line in f:
    if score(line[:14]) > score(line[14:]):
        player1 += 1

print player1
