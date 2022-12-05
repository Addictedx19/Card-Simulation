# deck.py

import random
from card import Card


class DeckOfCards:

    NUMBER_OF_CARDS = 52

    def __init__(self):
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUITES[count//13]))

    def shuffle(self):
        """Method to shuffle the deck of cards"""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Deal a card"""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            print('Deck is empty')
            return None

    def __str__(self):
        """String representation of the deck of cards"""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index+1) % 4 == 0:
                s += '\n'

        return s

    def __repr__(self):
        """String representation of the deck of cards"""
        s = ''

        for index in range(len(self._deck)):
            s += f'{index+1}, {repr(self._deck[index]):<45}'
            if (index+1) % 2 == 0:
                s += '\n'

        return s
