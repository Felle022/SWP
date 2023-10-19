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
'''


def draw_hand_crad(count):
    cards=np.arange(1,53)
    length=len(cards)-1
    for x in range(count):
        index=random.randint(1, length)
        cards[index], cards[length] = cards[length], cards[index]
        length = length - 1
    drawn_cards = cards[47:52]
    hand = np.zeros((2, 5))

    for x in range(len(drawn_cards)):
       hand[0][x]=drawn_cards[x]//14
       hand[1][x] = drawn_cards[x] % 14
    return hand


print(draw_hand_crad(5))