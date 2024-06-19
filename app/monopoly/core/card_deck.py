from django.utils.translation import gettext as _
from random import shuffle
from card import Card


class CardDeck(object):

    # property
    def __init__(self):
        self._index = 0
        self._cards = []
        self._cards.append(Card(_("Get One More Grace day "), 100, 0))
        self._cards.append(Card(_("Overspeed "), 200, 0))
        self._cards.append(Card(_("Autolab rank reward "), -100, 0))
        self._cards.append(Card(_("Illegal Parking "), 150, 0))
        self._cards.append(Card(_("Meet harry potter in Doherty Hall"), -150, 0))
        self._cards.append(Card(_("Host a fantastic Carnival"), -200, 0))
        self.shuffle()

    def insert(self, card):
        self._cards.append(card)

    def shuffle(self):
        shuffle(self._cards)

    def draw(self):
        self._index = (self._index + 1) % len(self._cards)
        if self._index == 0:
            self.shuffle()
        return self._cards[self._index]
