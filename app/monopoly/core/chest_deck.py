from django.utils.translation import gettext as _
from random import shuffle
from chest import Chest


class ChestDeck(object):

    # property
    def __init__(self):
        self._index = 0
        self._cards = []
        self._cards.append(Chest(_("Pay tuition in the amount "), -50, 0))
        self._cards.append(Chest(_("Bank error in your favor "), 200, 0))
        self._cards.append(Chest(_("Income tax refund "), 20, 0))
        self._cards.append(Chest(_("Vacation fund payment due date, get a "), 100, 0))
        self._cards.append(Chest(_("A visit to the doctor, pay "), -50, 0))
        self._cards.append(Chest(_("Pay hospitalization expenses in the amount of "), -100, 0))
        self._cards.append(Chest(_("Life insurance payment due date has arrived, get a "), 100, 0))
        self._cards.append(Chest(_("You came in second place in the beauty pageant, you're gonna get "), 10, 0))
        self._cards.append(Chest(_("For consulting services, you'll get "), 25, 0))
        self._cards.append(Chest(_("You make money on the sale of shares "), 50, 0))
        self._cards.append(Chest(_("You're getting an inheritance "), 100, 0))
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
