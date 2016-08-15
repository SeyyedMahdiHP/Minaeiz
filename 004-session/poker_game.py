import random


def deal(num, n=5, deck=[r+s for r in "23456789TJQKA" for s in "HDCS"]):
    random.shuffle(deck)
    return [deck[i*n:(i+1)*n] for i in range(num)]


def card_ranks(hand):
    return sorted(['__23456789TJQKA'.index(r) for r, s in hand], reverse=True)


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, ranks
    elif kind(4, ranks):
        return 7, kind(4, ranks), ranks
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, max(ranks)
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def play_poker(hands):
    return max(hands, key=hand_rank)


def flush(hand):
    return len(set([s for r, s in hand])) == 1


def straight(ranks):
    if ranks == [14, 5, 4, 3, 2]:
        return True
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r


def two_pair(ranks):
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and high_pair != low_pair:
        return high_pair, low_pair


def test():
    sf1 = ['2D', '3D', '4D', '5D', '6D']
    cr1 = ['3H', '4H', '9D', 'QC', '8S']
    st1 = [12, 11, 10, 9, 8]
    st2 = [14, 5, 4, 3, 2]
    fk = ['2D', '2H', '2S', '2C', 'TS']
    tk = ['TD', 'TH', 'TS', '6H', '9D']
    tp = [10, 10, 9, 3, 3]
    assert flush(sf1) is True
    assert card_ranks(cr1) == [12, 9, 8, 4, 3]
    assert straight(st1) is True
    assert straight(st2) is True
    assert kind(4, card_ranks(fk)) == 2
    assert kind(3, card_ranks(tk)) == 10
    assert two_pair(tp) == (10, 3)
    return "PASSED"

# print(test())


def hand_percentages(n=700*1000):
    hand_names = ["Straight flush", "Four of a kind", "Full house", "Flush", "Straight", "Three of a kind", "Two pair",
                  "One pair", "High card"]
    counts = [0] * 9
    for i in range(n // 10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%15s: %6.4f %%" % (hand_names[i], 100.*counts[8 - i]/n))

# hand_percentages()

l = [1, 2, 3, 4]
sl = [3, 2, 1, 4]
def my_shuffle(l):
    return "shuffled of l"




















