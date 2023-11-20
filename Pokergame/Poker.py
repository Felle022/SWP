import random
import numpy as np
import matplotlib.pyplot as plt

'''
0...Ace
1...Two
2...Three
3...four
4...funf
5...six
6...seven
7...eigeht
8...nine
9... ten
10... J
11... Q
12... K
'''

highest_street = False


def draw_hand_crad(count):
    cards = np.arange(1, 53)
    length = len(cards) - 1
    for x in range(count):
        index = random.randint(1, length)
        cards[index], cards[length] = cards[length], cards[index]
        length = length - 1
    drawn_cards = cards[47:52]
    hand = np.zeros((2, 5))

    for x in range(len(drawn_cards)):
        hand[0][x] = drawn_cards[x] // 13
        hand[1][x] = drawn_cards[x] % 13

    return hand


def check_pairs(hand):
    hand.sort()
    cards = []
    str_answer = ''
    for x in range(len(hand[1])): cards.append(hand[1][x])
    answer = check(cards, len(cards), str_answer)
    return answer


def check(cards, length, str_answer):
    for value in range(length):
        if cards.count(cards[value]) == 2:
            to_delete = cards[value]
            str_answer = str_answer + 'pair'
            if str_answer == 'pairpair':
                return 'two-pair'
            elif str_answer == 'three of a kindpair':
                return 'fullhouse'
            while to_delete in cards: cards.remove(to_delete)
            str_answer = check(cards, len(cards), str_answer)
            break
        elif cards.count(cards[value]) == 3:
            to_delete = cards[value]
            str_answer = str_answer + 'three of a kind'
            if str_answer == 'pairthree of a kind':
                return 'fullhouse'
            while to_delete in cards: cards.remove(to_delete)
            str_answer = check(cards, len(cards), str_answer)
            break
        elif cards.count(cards[value]) == 4:
            to_delete = cards[value]
            str_answer = 'quads'
            while to_delete in cards: cards.remove(to_delete)
            str_answer = check(cards, len(cards), str_answer)
            break
        elif len(cards) == 1:
            break
    return str_answer


def check_street(hand):
    hand.sort()
    cards = []
    global highest_street
    highest_street = False
    for x in range(len(hand[1])): cards.append(hand[1][x])
    lastcard = cards[0] - 1
    if cards == [0, 9, 10, 11, 12]: highest_street = True
    for card in cards:
        if card == lastcard + 1:
            lastcard = card
        else:
            return ''
    return 'straight'


def check_flush(hand):
    hand.sort()
    suits = []
    global highest_street
    for x in range(len(hand[0])): suits.append(hand[0][x])
    if suits.count(suits[0]) == 5 and highest_street == True:
        return 'royal flush'
    if suits.count(suits[0]) == 5:
        return 'flush'
    return ''


dic = {
    '': 0,
    'pair': 0,
    'two-pair': 0,
    'three of a kind': 0,
    'straight': 0,
    'flush': 0,
    'fullhouse': 0,
    'quads': 0,
    'straightflush': 0,
    'royal flush': 0

}
# Possibilities for 5card-Poker
posibilities = {
    '': 50.1177,
    'pair': 42.2569,
    'two-pair': 4.7539,
    'three of a kind': 2.1128,
    'straight': 0.3925,
    'flush': 0.1965,
    'fullhouse': 0.1441,
    'quads': 0.02401,
    'straightflush': 0.00139,
    'royal flush': 0.000154
}


def possibility(dic, turns):
    for x in range(turns):
        hand = draw_hand_crad(5)
        combination = check_street(hand) + check_flush(hand) + check_pairs(hand)
        if (combination == 'straightroyal flush'): combination = 'royal flush'
        dic[combination] = dic[combination] + 1
    for x in dic:
        dic[x] = dic[x] / turns * 100
    return dic


def plot_diagramm(dic1, dic2):
    plt.plot(list(dic1.keys()), list(dic1.values()), label='Dictionary 1')
    plt.plot(list(dic2.keys()), list(dic2.values()), label='Dictionary 2')

    # Füge Achsentitel und Diagrammlegende hinzu
    plt.xlabel('Keys')
    plt.ylabel('Werte')
    plt.legend()
    plt.show()


print(possibility(dic, 1000000))

#plot_diagramm(dic, posibilities)
