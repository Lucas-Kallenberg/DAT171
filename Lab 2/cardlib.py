import enum
import random


class PlayingCard():
    def __init__(self, suit):
        self.suit = suit

    def __lt__(self, other):
        return (self.get_value() < other.get_value())

    def __eq__(self, other):
        return (self.get_value() == other.get_value())


class Suit(enum.IntEnum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3

class NumberedCard(PlayingCard):
    def __init__(self,value, suit):
        super().__init__(suit)
        self.value = value

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__( suit)
        self.value = 11

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.vaue = 12
    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = 13

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = 1

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

class StandardDeck:
    def __init__(self):
        self.cards = []
        for s in Suit:
            for i in [2,11]:
                self.cards.append(NumberedCard(value=i,suit=s))
            self.cards.append(JackCard(suit=s))
            self.cards.append(QueenCard(suit=s))
            self.cards.append(KingCard(suit=s))
            self.cards.append(AceCard(suit=s))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)









