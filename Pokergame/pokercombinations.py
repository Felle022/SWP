import random
import numpy as np
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


def check_flush(hand,highest_street):
    hand.sort()
    suits = []
    for x in range(len(hand[0])): suits.append(hand[0][x])
    if suits.count(suits[0]) == 5 and highest_street == True:
        return 'royal flush'
    if suits.count(suits[0]) == 5:
        return 'flush'
    return ''